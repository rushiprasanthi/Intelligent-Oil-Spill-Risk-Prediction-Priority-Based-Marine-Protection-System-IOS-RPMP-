// frontend/map/map_init.js

// Make map truly global
window.map = L.map("map").setView([20, 78], 4);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "Leaflet | © OpenStreetMap"
}).addTo(window.map);
