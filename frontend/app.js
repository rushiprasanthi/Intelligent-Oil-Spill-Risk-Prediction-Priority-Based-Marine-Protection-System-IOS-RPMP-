const API_URL = "http://127.0.0.1:8000/simulate_spill";

async function simulateSpill(lat, lng) {
  const statusEl = document.getElementById("system-status");
  if (statusEl) statusEl.textContent = "Simulation Active";

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ lat: lat, lng: lng, spill_size: 0.8 })
    });

    if (!response.ok) {
      if (statusEl) statusEl.textContent = "Simulation failed";
      console.error("Simulation API returned", response.status);
      return;
    }

    const data = await response.json();
    // Update dashboard safely
    if (typeof window.updateDashboard === "function") window.updateDashboard(data);

    // Draw spill overlay if available
    if (typeof window.drawSpill === "function") {
      const radius = (data && data.simulation && data.simulation.spread_radius_km) || 0.5;
      window.drawSpill(lat, lng, radius);
    }

    if (statusEl) statusEl.textContent = "Simulation Complete";
  } catch (err) {
    if (statusEl) statusEl.textContent = "Simulation error";
    console.error("Simulation error:", err);
  }
}

// Expose for other scripts (non-module).
window.simulateSpill = simulateSpill;
