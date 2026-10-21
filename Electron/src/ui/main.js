import './leaflet-global.js'; // must stay first: exposes window.L for the plugins below
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import 'leaflet.markercluster';
import 'leaflet.markercluster/dist/MarkerCluster.css';
import 'leaflet.markercluster/dist/MarkerCluster.Default.css';
import 'leaflet-realtime';
import './style.css';

const RELAY_URL = 'ws://127.0.0.1:8765';   // websocket.py relay
const STALE_AFTER_MS = 10 * 60 * 1000;      // drop ships silent for 10 min
const cartoApiKey = import.meta.env.VITE_CARTO_API_KEY;

// ---------- map ----------
const map = L.map('map', { scrollWheelZoom: true }).setView([43.0, 34.0], 6);

L.tileLayer(`https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png?key=${cartoApiKey}`, {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
  subdomains: 'abcd',
  maxZoom: 20
}).addTo(map);

// ---------- helpers ----------
const esc = (s) =>
  String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

function shipIcon(heading) {
  const known = Number.isFinite(heading) && heading >= 0 && heading < 360;
  const html = known
    ? `<svg viewBox="0 0 24 24" width="20" height="20" style="transform:rotate(${heading}deg)"><path d="M12 2 L19 21 L12 17 L5 21 Z"/></svg>`
    : `<svg viewBox="0 0 24 24" width="14" height="14"><circle cx="12" cy="12" r="6"/></svg>`;
  return L.divIcon({ className: 'ship-icon', html, iconSize: [20, 20], iconAnchor: [10, 10] });
}

function label(p) {
  const parts = [esc(p.name && p.name !== 'Unknown' ? p.name : p.mmsi)];
  if (p.country) parts.push(esc(p.country));
  if (Number.isFinite(p.sog)) parts.push(`${p.sog.toFixed(1)} kn`);
  return parts.join(' &middot; ');
}

// ---------- ships layer ----------
// Clustering keeps nearby ships from overlapping; at max zoom, ships at the
// exact same spot fan out (spiderfy) when clicked.
const cluster = L.markerClusterGroup({
  maxClusterRadius: 40,
  spiderfyOnMaxZoom: true,
  chunkedLoading: true
}).addTo(map);

const realtime = L.realtime(
  (success) => success({ type: 'FeatureCollection', features: [] }), // push-only, never polled
  {
    start: false,
    container: cluster,
    getFeatureId: (f) => f.properties.mmsi, // one marker per ship, so no duplicates
    pointToLayer: (f, latlng) =>
      L.marker(latlng, { icon: shipIcon(f.properties.heading) }).bindTooltip(label(f.properties)),
    // Default update only moves the marker; we also refresh heading and label.
    updateFeature: (f, oldLayer) => {
      if (!oldLayer) return;
      const [lon, lat] = f.geometry.coordinates;
      oldLayer.setLatLng([lat, lon]);
      oldLayer.setIcon(shipIcon(f.properties.heading));
      oldLayer.setTooltipContent(label(f.properties));
      return oldLayer;
    }
  }
).addTo(map);

// ---------- live feed ----------
const seen = new Map(); // mmsi -> { feature, t }
const statusEl = document.getElementById('status');

function setStatus(text, ok) {
  statusEl.textContent = text;
  statusEl.dataset.ok = ok ? '1' : '0';
}

function connect() {
  setStatus('Connecting…', false);
  const ws = new WebSocket(RELAY_URL);

  ws.onopen = () => setStatus(`Live · ${seen.size} ships`, true);

  ws.onmessage = (e) => {
    let batch;
    try {
      batch = JSON.parse(e.data);
    } catch {
      return;
    }
    const now = Date.now();
    for (const f of batch) seen.set(f.properties.mmsi, { feature: f, t: now });
    realtime.update({ type: 'FeatureCollection', features: batch });
    setStatus(`Live · ${seen.size} ships`, true);
  };

  ws.onclose = () => {
    setStatus('Disconnected, retrying…', false);
    setTimeout(connect, 2000); // survives restarting websocket.py
  };
  ws.onerror = () => ws.close();
}
connect();

// remove ships that stopped transmitting
setInterval(() => {
  const cutoff = Date.now() - STALE_AFTER_MS;
  for (const [id, { feature, t }] of seen) {
    if (t < cutoff) {
      realtime.remove(feature);
      seen.delete(id);
    }
  }
}, 60_000);
