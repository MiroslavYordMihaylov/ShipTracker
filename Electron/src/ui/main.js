import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import './style.css';

const cartoApiKey = import.meta.env.VITE_CARTO_API_KEY;
const map = L.map('map', {
  scrollWheelZoom: true
}).setView([43.0, 34.0], 6);

L.tileLayer(`https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png?key=${cartoApiKey}`, {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
  subdomains: 'abcd',
  maxZoom: 20
}).addTo(map);