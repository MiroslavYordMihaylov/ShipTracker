// Leaflet plugins (markercluster, realtime) expect a global `L`.
// ES modules evaluate in import order, so importing this file first makes `L` available to them.
import L from 'leaflet';
window.L = L;
