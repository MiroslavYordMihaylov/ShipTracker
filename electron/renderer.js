// map-logic.js (renderer.js)

const initMap = () => {
    // Set up the Map
    const map = L.map('map').setView([51.94, 3.99], 12);

    // Dark Background
    L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png').addTo(map);

    // Nautical Layer
    L.tileLayer('https://tiles.openseamap.org/seamark/{z}/{x}/{y}.png').addTo(map);

    console.log("Maritime Map Initialized");
};

// Start the map when the window loads
window.onload = initMap;