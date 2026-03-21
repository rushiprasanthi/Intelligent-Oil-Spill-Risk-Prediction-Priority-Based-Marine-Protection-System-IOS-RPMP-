// frontend/ui/dashboard.js

function updateDashboard(data) {

  const zonesCount = data.zones_analysis ? 
    Object.keys(data.zones_analysis).length : 0;
  const hotspotsCount = data.hotspots ? data.hotspots.length : 0;
  
  const zonesEl = document.getElementById('zones-count');
  const hotspotsEl = document.getElementById('hotspots-count');
  
  if (zonesEl) zonesEl.textContent = zonesCount;
  if (hotspotsEl) hotspotsEl.textContent = hotspotsCount;

  // ─── PRIORITY ──────────────────────────────
  const priority = data.risk?.priority;
  const priorityLabel = data.risk?.priority_label;

  const priorityTextEl = document.getElementById("priority-text");
  if (priorityTextEl) {
    priorityTextEl.textContent = `${priority || "–"} - ${priorityLabel || "–"}`;
  }

  const banner = document.getElementById("priority-banner");
  if (banner) {
    banner.textContent = priority || "–";
    banner.className = "";
    if (priority === "P1") banner.classList.add("p1");
    if (priority === "P2") banner.style.background = "#ff9800";
    if (priority === "P3") banner.style.background = "#ffd54f";
  }

  // ─── DEPLOYMENT ─────────────────────────────
  document.getElementById("port").textContent =
    data.deployment?.nearest_port?.name || "–";

  const dist = data.deployment?.nearest_port?.distance_km;
  document.getElementById("distance").textContent =
    typeof dist === "number" ? dist.toFixed(1) : "–";

  const eta = data.deployment?.eta_hours;
  document.getElementById("eta").textContent =
    typeof eta === "number" ? eta.toFixed(2) : "–";

  document.getElementById("ships").textContent =
    data.deployment?.ships_required ?? "–";

  document.getElementById("direction").textContent =
    data.simulation?.projected_direction_deg !== undefined
      ? `${data.simulation.projected_direction_deg}°`
      : "–";

  // ─── DAMAGE ────────────────────────────────
  document.getElementById("eco-impact").textContent =
    data.damage_control?.ecosystem_impact_percent ?? "–";

  document.getElementById("damage-control").textContent =
    data.damage_control?.damage_controlled_percent ?? "–";

  const loss = data.economic_loss_musd;
  document.getElementById("economic-loss").textContent =
    typeof loss === "number" ? loss.toFixed(2) : "–";

  document.getElementById("fishery").textContent =
    data.damage_control?.fishery_area_sqkm ?? "–";

  // ─── ALERT STATUS (FIXED) ───────────────────
  const alertEl = document.getElementById("email-status");

  if (alertEl) {
    if (typeof data.alert === "string") {
      alertEl.textContent = data.alert;
    } else if (data.alert && typeof data.alert.status === "string") {
      alertEl.textContent = data.alert.status;
    } else {
      alertEl.textContent = "";
    }
  }

  // ─── EXPLANATION ────────────────────────────
  const explanationDiv = document.getElementById("explanation");
  if (explanationDiv) {
    explanationDiv.innerHTML = "";
    const factors = data.risk?.explanation?.factors || [];
    factors.forEach(factor => {
      const p = document.createElement("p");
      p.textContent = "• " + factor;
      explanationDiv.appendChild(p);
    });
  }

  // ─── HOTSPOTS ───────────────────────────────
  if (!window.hotspotMarkers) window.hotspotMarkers = [];

  window.hotspotMarkers.forEach(m => {
    if (window.map.hasLayer(m)) window.map.removeLayer(m);
  });
  window.hotspotMarkers = [];

  const zones = Array.isArray(data.zones_analysis)
    ? data.zones_analysis
    : [];

  const activeHotspots = zones.filter(z => z.is_hotspot === true);

  const hotspotsList = document.getElementById("hotspots-list");
  if (!hotspotsList) return;

  hotspotsList.innerHTML = "";

  if (activeHotspots.length === 0) {
    hotspotsList.innerHTML = "No active hotspot zones.";
  } else {

    activeHotspots.forEach(z => {

      const html =
        `<div class="hotspot-marker">
           <div class="hotspot-pulse"></div>
         </div>`;

      const icon = L.divIcon({
        className: "",
        html: html,
        iconSize: [14, 14]
      });

      if (typeof z.lat === "number" && typeof z.lng === "number") {

        const marker = L.marker(
          [z.lat, z.lng],
          { icon, zIndexOffset: 5000 }
        ).addTo(window.map);

        marker.bindPopup(
          `<b>🔥 HOTSPOT ZONE</b><br>
           Zone: ${z.name}<br>
           Distance: ${z.distance_km ?? "–"} km`
        );

        window.hotspotMarkers.push(marker);
      }
    });
  }
}
