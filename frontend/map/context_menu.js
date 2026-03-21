// frontend/map/context_menu.js

// Global spill marker
window.spillMarker = null;

(function () {

  if (!window.map) {
    console.error("Map not initialized.");
    return;
  }

  const map = window.map;

  const spillIcon = L.divIcon({
    className: 'spill-marker',
    html: '<div style="background:red;width:16px;height:16px;border-radius:50%;border:2px solid darkred;"></div>',
    iconSize: [16, 16],
    iconAnchor: [8, 8]
  });

  function placeSpill(lat, lng) {

    // Remove previous spill marker
    if (window.spillMarker && map.hasLayer(window.spillMarker)) {
      map.removeLayer(window.spillMarker);
    }

    // Create new marker
    window.spillMarker = L.marker([lat, lng], {
      icon: spillIcon,
      zIndexOffset: 10000
    }).addTo(map);

    window.spillMarker.bindTooltip("Spill", {
      permanent: true,
      direction: "top",
      offset: [0, -10]
    });

    if (typeof window.simulateSpill === "function") {
      window.simulateSpill(lat, lng);
    } else {
      console.error("simulateSpill is not available on window.");
    }
  }

  // Attach single context menu listener
  map.off("contextmenu");

  map.on("contextmenu", function (e) {
    const confirmMark = confirm("Mark this location as Spill?");
    if (!confirmMark) return;

    placeSpill(e.latlng.lat, e.latlng.lng);
  });

})();
