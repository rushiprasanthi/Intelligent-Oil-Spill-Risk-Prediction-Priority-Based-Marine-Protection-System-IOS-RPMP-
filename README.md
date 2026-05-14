```markdown
# 🌊 IOS-RPMP
**Intelligent Oil-Spill Risk Prediction & Priority-Based Marine Protection System**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#license) [![Python](https://img.shields.io/badge/Python-3.11+-blue)](#technical-stack) [![FastAPI](https://img.shields.io/badge/FastAPI-production-ready-green)](#technical-stack)

Predict. Prioritize. Protect.

---

Table of Contents
- [Project Overview](#project-overview)
- [Core Features](#core-features)
- [System Architecture](#system-architecture)
- [Technical Stack](#technical-stack)
- [Repository Layout (Folder Structure)](#repository-layout-folder-structure)
- [Execution & Pipeline Workflow](#execution--pipeline-workflow)
- [API Reference](#api-reference)
- [Installation & Local Development](#installation--local-development)
- [Running the System (Dev / Prod)](#running-the-system-dev--prod)
- [Scalability & Engineering Considerations](#scalability--engineering-considerations)
- [Challenges & Engineering Decisions](#challenges--engineering-decisions)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Acknowledgements](#acknowledgements)

---

## Project Overview

IOS‑RPMP is a decision-support prototype that simulates surface oil-spill spread on a lightweight 2D grid, evaluates ecological exposure, scores risk, and produces priority-based deployment recommendations for containment resources.

Real-world problem:
- Oil spills propagate rapidly and can reach sensitive coastal ecosystems (coral reefs, mangroves, fish breeding grounds) long before field teams can be optimally deployed.
- Decision-makers need an explainable, fast, and geospatially-aware system to predict impact zones, prioritize response, and recommend logistics.

Why this project matters:
- It provides a reproducible, auditable simulation and prioritization stack suitable for emergency response drills, academic studies, and early-stage operational proof-of-concepts.
- Emphasizes explainability, deterministic behavior for repeatable simulations, and integration points for future AI and real-time sensor data.

Engineering goals:
- Lightweight, deterministic simulation that runs on laptops and edge devices (Raspberry Pi).
- Clear separation: simulation, risk scoring, deployment intelligence, alerting.
- API-first backend to enable integration with dashboards, automation, and orchestration systems.

---

## Core Features

High-level capabilities implemented and documented in the codebase:

- Interactive geospatial frontend (Leaflet + OpenStreetMap) for spill initiation and visual playback.
- 2D grid-based Oil Spill Simulation (diffusion + wind-driven advection).
- Simplified time-stepped simulation clock for deterministic progression.
- Risk scoring engine combining sensitivity of protected zones with spread metrics and time-to-impact.
- Priority classification (P1/P2/P3) with policy-driven deployment recommendations (ship allocation, nearest ports, ETA).
- Zones intelligence: evaluates predefined ecological hotspots against simulation projection.
- Emergency alerting hooks — email service for critical (P1) events (fail-safe: email errors do not stop the pipeline).
- Well-structured FastAPI backend exposing a simulation endpoint for automation and integration.
- Lightweight deployable stack that runs on development machines and low-power devices.

Operational engineering highlights:
- Single-source-of-truth response document returned by the API containing simulation, risk, deployment, damage-control estimates, zone analysis, and meta-trace.
- Deterministic defaults for stability (fixed wind in demo mode, fixed time-steps) enabling reproducible tests and regression tracking.

---

## System Architecture

High-level ASCII diagram (request & processing flow):

```text
+------------------+       POST /simulate_spill       +------------------+
|  Frontend (UI)   |  ----------------------------->  |  FastAPI Backend |
|  Leaflet Map     |                                   |  (uvicorn)       |
+------------------+                                   +--------+---------+
                                                                 |
                                                                 |  Controller: handle_spill
                                                                 v
                                     +-------------------+  +------------------+
                                     | Simulation Engine |  | Zones Evaluation |
                                     | (diffusion + adv) |  | (sensitivity DB) |
                                     +-------------------+  +------------------+
                                               |                     |
                                               v                     v
                                      +-------------------------------+
                                      |    Risk Analysis Engine       |
                                      |  (exposure, risk_score, ETA)  |
                                      +-------------------------------+
                                                       |
                                                       v
                                      +-------------------------------+
                                      | Deployment Intelligence Layer |
                                      |  (nearest-port, ETA, ships)   |
                                      +-------------------------------+
                                                       |
                                                       v
                                      +-------------------------------+
                                      |  Alerts / Email Service       |
                                      +-------------------------------+
                                                       |
                                                       v
                                      +-------------------------------+
                                      | API Response (single JSON doc)|
                                      +-------------------------------+
```

Component responsibilities:
- Frontend: map-driven UX — creates spill events and visualizes simulation frames.
- API Router: lightweight mapping of requests to controller flow.
- Spill Controller: orchestrates simulation → risk → deployment → alerts; composes final response.
- Simulation Engine: core 2D grid model composed of diffusion & advection steps; provides spread radius and projected direction.
- Risk Engine: computes exposure probability, time-to-impact, and a risk score (explainable formula kept simple for clarity).
- Deployment Engine: nearest-port calculations, ETA and ship-allocation heuristics.
- Zones Evaluator: spatial intersection of spread projection with predefined sensitive zones dataset.
- Alert Service: sends structured emergency emails on critical events without failing the pipeline when notification delivery fails.

Request lifecycle (POST /simulate_spill):
1. Request validated and deserialized into `SpillRequest` (Pydantic model).
2. Simulation engine runs a short, deterministic time-series (8 steps in demo).
3. Risk engine consumes simulation output & spill meta to compute exposure and priority.
4. Deployment engine computes practical response recommendations.
5. Zones engine evaluates impacted hotspots.
6. Controller composes a comprehensive JSON response and triggers alerts conditionally.

---

## Technical Stack

Why these choices were made:
- Python — rapid prototyping, abundant scientific libraries, readability for reviewers and domain experts.
- FastAPI — modern, fast, type-safe web API framework with automatic OpenAPI docs; ideal for exposing simulation services.
- NumPy/SciPy — efficient numerical operations and vectorized array manipulation critical to grid-based simulation.
- Leaflet.js & OpenStreetMap — widely used, low-dependency mapping stack for highly interactive geospatial UIs.
- PostgreSQL + PostGIS (optional) — for production: robust spatial queries and disk-based geo-indexing for zones/ports.
- Email service — simple notification integration for prototype alerting; pluggable for real SMTP or third-party providers.
- Uvicorn — ASGI server recommended for FastAPI.

Tech stack summary:

| Layer        | Library / Tool        | Purpose |
|--------------|-----------------------|---------|
| API          | FastAPI, Uvicorn      | HTTP API, routing, fast async server |
| Simulation   | NumPy                 | Grid algebra, diffusion/advection |
| Frontend     | HTML/CSS/JS, Leaflet  | Interactive map and visualization |
| Data         | JSON datasets (ports, zones) | Local demo corpora for ports/zones |
| Optional DB  | PostgreSQL + PostGIS  | Production spatial storage & queries |
| Dev/Infra    | Git, VS Code launch   | Development workflow |
| ML (future)  | scikit-learn / TF     | Severity prediction & time-series models |

---

## Repository Layout (recommended + actual)

Professional project tree (reflects repository):

```text
IOS-RPMP/
├── backend/
│   ├── main.py                      # FastAPI application entrypoint
│   ├── api_routes.py                # Router + endpoint bindings
│   ├── controllers/                 # Controllers orchestrating engines
│   │   ├── spill_controller.py
│   │   ├── simulation_controller.py
│   │   ├── risk_controller.py
│   │   ├── deployment_controller.py
│   │   └── zones_controller.py
│   ├── services/                    # Integrations (email, notifications)
│   │   └── email_service.py
│   └── schemas/                      # Pydantic models / request/response contracts
├── simulation/
│   ├── spread_model.py              # High-level OilSpillSimulation class
│   ├── grid.py                      # OceanGrid data structures and resolution config
│   ├── diffusion.py                 # Diffusion kernel implementations
│   ├── advection.py                 # Wind-driven advection transforms
│   └── timestep.py                  # SimulationClock for deterministic ticks
├── frontend/
│   ├── index.html                   # Map UI for simulation interactions
│   ├── script.js                    # Map event handlers and visualizer
│   └── style.css
├── data/
│   ├── ports.json                   # Demo ports dataset
│   └── zones.json                   # Demo sensitive zone dataset
├── docs/                            # Optional project documentation / diagrams
├── tests/                           # Unit / integration tests (skeleton)
├── simulation_test.py               # Example simulation test script
├── README.md
└── requirements.txt
```

Key files explained:
- `backend/main.py`: Creates FastAPI app, configures CORS, mounts routes.
- `backend/api_routes.py`: Defines `/simulate_spill` endpoint and wiring.
- `backend/controllers/spill_controller.py`: Orchestrates the end-to-end simulation run and composes the final envelope returned to clients.
- `simulation/spread_model.py`: Encapsulates the diffusion + advection simulation loop.
- `simulation/diffusion.py`, `simulation/advection.py`: Kernel implementations — keep the model modular for future replacement with higher-fidelity physics or ML surrogates.
- `data/ports.json`, `data/zones.json`: Lightweight demo datasets used by the deployment and zones evaluators.

---

## Execution & Pipeline Workflow

Step-by-step runtime flow (development, default behavior):
1. Client posts a spill event to `/simulate_spill` with at minimum geographical coordinates (lat, lng).
2. `spill_controller.handle_spill` is invoked and:
   - Initializes/executes the OilSpillSimulation for N deterministic steps (currently 8).
   - Calls the Risk Analysis engine to convert simulation state into exposure probability, ETA and risk score.
   - Calls Deployment Intelligence to compute nearest ports, ETA and recommended response allocation.
   - Evaluates overlap with sensitive zones and computes zone-level metrics (sensitivity, impact estimate).
   - Calculates derived metrics (damage controlled %, economic loss estimate, fishery area affected).
   - Conditionally triggers emergency email notifications for P1 events (non-blocking).
3. Controller returns a single JSON document containing:
   - meta, simulation, risk, deployment, damage_control, zones_analysis, alert status.

Scheduling & orchestration considerations:
- Simulation is currently synchronous and short-running (seconds). For longer or batch simulations, the architecture allows wrapping simulations in a background worker (Celery / RQ) and exposing a job API for asynchronous processing.
- The controller is intentionally strict about not failing on optional integrations (e.g., email), keeping core path robust.

---

## API Reference

POST /simulate_spill
- Description: Run the decision-support pipeline for a new spill event.
- Content-Type: application/json
- Request contract: Pydantic model `SpillRequest` (example fields below). The server will apply sensible defaults for environment values if missing.

Example request (minimal):
```json
{
  "lat": 21.4000,
  "lng": 78.0000
}
```

Example request (with optional overrides — prototype supports these keys but will apply defaults where necessary):
```json
{
  "lat": 21.4000,
  "lng": 78.0000,
  "start_time_utc": "2026-05-14T06:00:00Z",
  "volume_liters": 5000,
  "wind_speed_kmh": 30,           // optional override; engine currently uses demo constants
  "wind_direction_deg": 60
}
```

Example response (abridged):
```json
{
  "meta": {
    "simulation_id": "SIM-001",
    "timestamp_utc": "2026-05-14T12:34:56Z",
    "mode": "decision-support-prototype"
  },
  "simulation": {
    "spread_radius_km": 12.34,
    "wind_speed": 30,
    "wind_direction": 60,
    "projected_direction_deg": 60,
    "time_hours": 8
  },
  "risk": {
    "exposure": 0.42,
    "risk_score": 3.7,
    "priority": "P2",
    "impact_eta_hours": 4.2
  },
  "deployment": {
    "nearest_port": "Port A",
    "distance_km": 85.2,
    "estimated_arrival_hours": 6.9,
    "recommended_ships": 2
  },
  "damage_control": {
    "estimated_control_percent": 64,
    "ecosystem_impact_percent": 50.1,
    "fishery_area_sqkm": 478.6
  },
  "zones_analysis": [
    {
      "zone_id": "Z-001",
      "name": "Coral Bay",
      "sensitivity": 9,
      "exposure_probability": 0.73,
      "predicted_impact_time_hours": 3.5
    }
  ],
  "economic_loss_musd": 28.75,
  "alert": {
    "status": "ℹ Monitoring only — no alert issued"
  }
}
```

Notes:
- The prototype response contains human-friendly estimates designed for decision-support and demonstrations. All numerical heuristics are documented in code and intentionally conservative for demo stability.

---

## Installation & Local Development

Prerequisites:
- Python 3.11+ (recommended)
- Git
- Node / browser (for frontend static files; Node not required unless you add tooling)
- (Optional) PostgreSQL + PostGIS for production spatial datasets

Clone repository:
```bash
git clone https://github.com/rushiprasanthi/Intelligent-Oil-Spill-Risk-Prediction-Priority-Based-Marine-Protection-System-IOS-RPMP-.git
cd Intelligent-Oil-Spill-Risk-Prediction-Priority-Based-Marine-Protection-System-IOS-RPMP-
```

Create and activate virtual environment:
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

Install backend dependencies:
```bash
pip install -r backend/requirements.txt
```

If `requirements.txt` is not present or you need to pin versions, the primary packages are:
```bash
pip install fastapi uvicorn numpy scipy
```

Frontend:
- The frontend is static and served by a static file server for local development (Python's http.server is sufficient).

Datasets:
- `data/ports.json` and `data/zones.json` are used by the deployment and zones evaluators. Replace with PostGIS-backed lookups in production.

---

## Running the System

Development (local):

1. Start backend (auto-reload):
```bash
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

2. Start frontend (static):
```bash
# from repository root
cd frontend
python -m http.server 5500
# Frontend served at: http://127.0.0.1:5500/
```

3. Send a test request:
```bash
curl -X POST "http://127.0.0.1:8000/simulate_spill" \
  -H "Content-Type: application/json" \
  -d '{"lat":21.4,"lng":78.0}'
```

Production (recommended approach):
- Containerize backend (add a Dockerfile) and run with an ASGI server (gunicorn + uvicorn workers) behind a load balancer.
- Use managed Postgres + PostGIS for zone/port persistence and indexing.
- Use an async task queue (Celery/RQ) for long-running or batched simulations and for notification retries.

---

## Scalability & Engineering Considerations

Current prototype design is intentionally synchronous and single-process. For production-readiness consider the following enhancements:

1. Horizontal scaling:
   - Containerize the API (Docker) and run multiple replicas behind a load-balancer. Keep simulation stateless or persist job state to a database/storage layer.
   - Use persistent job queues for longer runs (Celery with Redis/RabbitMQ or cloud-managed queues).

2. Asynchronous processing:
   - For heavy simulations or batch runs, convert controller flows to asynchronous jobs and return job IDs with a polling or webhook-based completion model.

3. Spatial storage & queries:
   - Move zones & ports into PostGIS for spatial indexing and efficient nearest-neighbor / intersection queries at scale.

4. Caching & performance:
   - Cache frequent spatial queries (e.g., expensive polygon intersection results).
   - Use NumPy vectorized operations (already leveraged) and avoid Python-level loops in hot code paths.
   - Use memory-mapped arrays or Numba/Cython if simulation kernels become a bottleneck.

5. Fault tolerance & retries:
   - Wrap external integrations (email, SMS) with retry policies and circuit-breakers.
   - Implement idempotency keys for job submission to avoid duplicate runs.

6. Monitoring & observability:
   - Add structured logging (JSON), distributed tracing, and metrics (Prometheus + Grafana) for performance & SLA tracking.

7. Distributed simulation:
   - For large-scale simulations, partition the grid spatially and run across workers with halo-exchange (MPI-like or distributed compute frameworks).

---

## Challenges & Engineering Decisions

Key trade-offs made:
- Explainability vs. fidelity: The simulation uses a diffusion + advection approximation that favors transparency and speed over full fluid dynamics fidelity (Navier–Stokes). This makes the system suitable for decision-support and educational use rather than operational hydrodynamic forecasting.
- Deterministic demo defaults: Using fixed winds and a fixed 8-hour demo run ensures reproducibility for tests and demos. Production would require ingesting real-time environmental data (wind, currents).
- Non-blocking integrations: Alerting is designed to be non-blocking — notification failures do not affect the core response to preserve the availability of the API.
- Lightweight datasets: Demo zones and ports are local JSON files to simplify onboarding. Production should migrate this data to a spatial DB.

Challenges addressed:
- Building a reproducible, auditable pipeline that produces a single source of truth for stakeholders (simulation + risk + deployment).
- Keeping the simulation modular so that future physics or ML layers can be swapped in with minimal disruption.

---

## Future Improvements

Prioritized roadmap for maturing the system:

- Replace local datasets with PostGIS-backed spatial store for robust querying and scale.
- Add containerization + CI/CD:
  - Dockerfile for backend
  - docker-compose for local orchestration
  - GitHub Actions pipelines for linting, tests, and image builds
- Asynchronous job orchestration:
  - Celery/RQ with Redis or a cloud queue for long-running simulations and retries
- Real-time data integration:
  - Wind & ocean current APIs (NOAA, Copernicus)
  - Satellite imagery ingestion for verification & automated updates
- ML-enhanced predictive layer:
  - Train models (Random Forest / LightGBM / LSTM) for spill escalation, trajectory emulation, and severity scoring
  - ML model explainability (SHAP) for decisions
- Monitoring and observability:
  - Prometheus metrics, Grafana dashboard, and ELK stack for logs
- Authentication & RBAC:
  - API keys and OAuth for controlled access, role-based views for responders and analysts
- Multi-tenant deployment:
  - Namespacing simulations per agency and support for region-specific data
- Real-time analytics & web sockets:
  - Stream simulation frames to UIs via WebSocket for live playback and team collaboration features

---

## Contribution & Code of Conduct

Contributions are welcome. Suggested contribution workflow:
1. Fork the repo.
2. Create a feature branch named `feat/<short-desc>` or `fix/<short-desc>`.
3. Write tests for new logic (simulation kernels, risk scoring).
4. Open a pull request with a clear description and design rationale.

Please follow conventional commits and include design considerations for any changes to the risk/deployment heuristics.

---

## Development Tips & Testing

- Use `simulation_test.py` as a starting point for automation and unit tests for simulation kernels.
- Keep numerical thresholds and constants centralized (e.g., grid resolution, diffusion coefficients) to simplify experimentation.
- Add reproducible seeds or deterministic initialization if adding stochastic elements later.

---

## License

MIT License — see the `LICENSE` file for details.

---

## Author

Parvatham Bhavanarushi  
Project maintained by: rushiprasanthi (GitHub)

---

## Acknowledgements

- Prototype geospatial UI powered by Leaflet and OpenStreetMap imagery.
- Numerical kernels and array ops leverage NumPy for performance and clarity.

---

Appendix — Quick Commands

Start backend (dev):
```bash
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

Start frontend (static dev server):
```bash
cd frontend
python -m http.server 5500
# open http://127.0.0.1:5500/
```

Run a sample simulation via curl:
```bash
curl -X POST "http://127.0.0.1:8000/simulate_spill" \
  -H "Content-Type: application/json" \
  -d '{"lat":21.4,"lng":78.0}'
```

---
- Draft OpenAPI documentation (schema examples) for the `SpillRequest` and `SpillAssessmentResult` contracts.
- Add a short CONTRIBUTING.md and skeleton GitHub Actions workflow for CI.
```
