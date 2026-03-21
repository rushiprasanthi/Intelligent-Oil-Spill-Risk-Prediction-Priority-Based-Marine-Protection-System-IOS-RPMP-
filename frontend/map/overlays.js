let spillCircle = null;

function drawSpill(lat, lng, radiusKm) {
  if (spillCircle) {
    window.map.removeLayer(spillCircle);
  }

  spillCircle = L.circle([lat, lng], {
    radius: radiusKm * 1000,
    color: "red",
    fillColor: "#ff0000",
    fillOpacity: 0.3
  }).addTo(window.map);
}
