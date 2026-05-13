# 🌊 IOS-RPMP

## Intelligent Oil Spill Risk Prediction & Priority-Based Marine Protection System

> AI-assisted marine environmental defense intelligence platform for predictive oil spill simulation, ecological risk prioritization, deployment optimization, and operational response planning.

---

# 🚀 Project Overview

IOS-RPMP is a physics-inspired, simulation-driven marine emergency decision-support system designed to improve oil spill response through predictive intelligence and priority-based environmental protection.

The system combines:

* 🌍 Real-world geospatial interaction
* 🌊 Dynamic oil spill spread simulation
* 🟡 Sensitive marine zone intelligence
* 📊 Ecological risk scoring
* 🚢 Smart deployment recommendations
* 📧 Emergency alert generation
* 🧠 AI-assisted severity prediction (future-ready architecture)

Unlike traditional reactive cleanup systems, IOS-RPMP focuses on:

> **Predicting environmental impact before ecological damage escalates.**

Based on the documented IOS-RPMP implementation and architecture specification. 

---

# 🎯 Problem Statement

Oil spills spread rapidly across ocean surfaces, damaging:

* Coral reefs
* Marine ecosystems
* Mangrove forests
* Fish breeding zones
* Coastal economies
* Tourism industries

### Current Limitation

Most existing systems respond only after oil reaches environmentally sensitive regions.

This delay causes:

* irreversible ecosystem damage
* delayed containment response
* poor deployment prioritization
* inefficient logistics allocation

---

# 💡 Proposed Solution

IOS-RPMP transforms marine spill response into:

```text id="r5i6w7"
Reactive Cleanup
        ↓
Predictive Intelligence
        ↓
Priority-Based Marine Protection
```

The system predicts:

* spill spread direction
* exposure probability
* ecological threat severity
* response urgency
* containment strategy
* operational deployment planning

---

# 🧠 Core Features

---

# 🌍 1. Real-World Interactive Map

Built using:

* Leaflet.js
* OpenStreetMap

### Features

* Real geographic coordinates
* Zoomable Earth visualization
* Right-click spill simulation
* Real-time marine interaction
* Spill initiation at exact latitude/longitude

---

# 🌊 2. Oil Spill Simulation Engine

The simulation engine uses:

* 2D grid-based diffusion
* directional wind bias
* iterative spread propagation
* physics-inspired advection approximation

### Simulation Model

```text id="g1h2i3"
Diffusion + Directional Advection
```

### Capabilities

* real-time execution
* directional spill movement
* animated spread visualization
* lightweight computation
* laptop-level performance

The model is intentionally:

* explainable
* computationally feasible
* hackathon-runnable
* scientifically inspired

NOT a full Navier–Stokes ocean solver.

---

# 🌬 3. Wind-Driven Directional Spread

Spill propagation dynamically changes based on:

* wind direction
* wind speed
* directional vectors
* spread velocity

Directional drift creates realistic spill movement patterns across the ocean surface.

---

# 🟡 4. Sensitive Zone Intelligence Layer

Predefined ecological protection zones include:

* Coral reefs
* Mangroves
* Marine protected areas
* Fish breeding zones
* Tourism coastal regions

Each zone contains:

* Sensitivity Index (1–10)
* Ecological impact weight
* Economic value score
* Recovery difficulty rating

---

# 📊 5. Risk Scoring Engine

The system dynamically calculates environmental risk using:

Risk = \frac{Sensitivity \times SpreadSpeed \times ExposureProbability}{TimeToImpact}

### Outputs

* Risk Score
* Exposure Probability
* Impact ETA
* Threat Severity
* Priority Classification

---

# 🚨 6. Priority Classification

| Priority | Meaning                     | Action                |
| -------- | --------------------------- | --------------------- |
| P1       | Immediate ecological threat | Immediate containment |
| P2       | Moderate threat             | Prepare deployment    |
| P3       | Low threat                  | Monitoring            |

---

# 🚢 7. Deployment Recommendation Engine

The deployment intelligence module calculates:

* nearest response port
* deployment distance
* estimated arrival time
* recommended ship allocation

### Rule-Based Allocation

| Risk Level | Ships Required |
| ---------- | -------------- |
| High       | 3 Ships        |
| Medium     | 2 Ships        |
| Low        | 1 Ship         |

The system uses:

* geographic distance calculations
* ETA estimation
* logistics-aware recommendations

---

# 📉 8. Damage Control Estimation

Containment effectiveness is estimated using:

DamageControlled% = (1 - ExposureProbability) \times 100

Adjusted dynamically using:

* response timing
* ETA vs impact time
* deployment efficiency

---

# 📧 9. Emergency Alert System

The system generates structured emergency summaries including:

* spill coordinates
* priority zones
* deployment recommendations
* containment efficiency
* estimated arrival time
* recommended response action

---

# 🧠 10. AI Severity Prediction Layer (Future Scope)

IOS-RPMP architecture supports future AI integration for:

* environmental severity classification
* spill escalation prediction
* response optimization

Potential models:

* Random Forest
* Gradient Boosting
* LSTM time-series prediction

---

# 🧱 System Architecture

```text id="z9x8c7"
User Interaction Layer
        ↓
Spill Event Trigger
        ↓
Environmental Simulation Engine
        ↓
Exposure Probability Assessment
        ↓
Risk & Priority Engine
        ↓
Deployment Intelligence Layer
        ↓
Damage Control Estimation
        ↓
Dashboard + Alerts + API Output
```

Architecture derived from IOS-RPMP implementation documentation. 

---

# 🖥️ Frontend Features

### Interactive Dashboard Includes

✔ Animated spill spread
✔ Real-world map visualization
✔ Sensitive zone overlays
✔ Wind direction indicators
✔ Priority zone highlighting
✔ Deployment recommendation panel
✔ Damage estimation metrics
✔ Real-time analytics dashboard
✔ Emergency simulation workflow

---

# 🖱️ Updated Frontend Interaction Workflow

The frontend interaction system uses:

* Leaflet.js right-click events
* custom context-menu interaction
* real-world spill coordinate placement

### Workflow

```text id="f6d5s4"
RIGHT CLICK ON MAP
        ↓
Custom Context Menu Appears
        ↓
Select "Simulate Spill"
        ↓
Red Spill-Origin Marker Added
        ↓
Simulation Pipeline Starts
        ↓
Risk + Deployment + Dashboard Updates
```

This upgraded interaction replaces the old left-click confirmation flow. 

---

# 🛠️ Technology Stack

## Frontend

* HTML5
* CSS3
* JavaScript
* Leaflet.js

## Backend

* Python
* FastAPI

## Simulation Layer

* NumPy
* SciPy

## Database (Optional)

* PostgreSQL
* PostGIS

## AI/ML Layer (Future Scope)

* Scikit-learn
* TensorFlow

---

# 📂 Recommended Project Structure

```text id="q1w2e3"
IOS-RPMP/
│
├── backend/
│   ├── main.py
│   ├── simulation/
│   ├── risk_engine/
│   ├── deployment/
│   ├── alerts/
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── assets/
│
├── datasets/
│   ├── ports.json
│   └── zones.json
│
├── README.md
└── .vscode/
```

---

# ⚙️ Local Execution Setup

---

# ▶️ Frontend Execution

Navigate to the frontend folder and run:

```bash id="frontendcmd01"
python -m http.server 5500
```

### Frontend URL

```text id="frontendurl01"
http://127.0.0.1:5500
```

### Frontend Entry File

```text id="frontendfile01"
frontend/index.html
```

### Main Frontend Files

```text id="frontendfiles02"
frontend/
├── index.html
├── style.css
├── script.js
└── assets/
```

---

# ▶️ Backend Execution

Run the FastAPI backend server:

```bash id="backendcmd01"
uvicorn backend.main:app --reload
```

### Backend API URL

```text id="backendurl01"
http://127.0.0.1:8000
```

### Main Backend Entry File

```text id="backendfile01"
backend/main.py
```

---

# ▶️ Full Local Startup Workflow

## Step 1 — Start Backend

Open terminal 1:

```bash id="fullrun01"
uvicorn backend.main:app --reload
```

---

## Step 2 — Start Frontend

Open terminal 2:

```bash id="fullrun02"
python -m http.server 5500
```

---

## Step 3 — Open Browser

Open:

```text id="fullrun03"
http://127.0.0.1:5500/frontend/
```

---

# ▶️ VS Code Launch Configuration

Create:

```text id="launchfile01"
.vscode/launch.json
```

Add:

```json id="launchjson01"
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Run IOS-RPMP Backend",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "backend.main:app",
        "--reload",
        "--host",
        "127.0.0.1",
        "--port",
        "8000"
      ],
      "jinja": true
    }
  ]
}
```

---

# 🍓 Raspberry Pi Deployment

IOS-RPMP is optimized for lightweight deployment and can run on Raspberry Pi 4.

## Recommended Hardware

* Raspberry Pi 4 (4GB+)
* Raspberry Pi OS
* Python 3.11+

---

# 📦 Raspberry Pi Installation

## Install Dependencies

```bash id="rpi01"
sudo apt update
sudo apt install python3-pip git
```

---

## Clone Repository

```bash id="rpi02"
git clone https://github.com/your-repo/IOS-RPMP.git
cd IOS-RPMP
```

---

## Install Backend Packages

```bash id="rpi03"
pip3 install -r backend/requirements.txt
```

---

## Run Backend

```bash id="rpi04"
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

---

## Access From Browser

```text id="rpi05"
http://<RASPBERRY_PI_IP>:8000
```

---

# 📦 API Endpoint

## POST `/simulate_spill`

### Example Response

```json id="apiresponse01"
{
  "spill": {...},
  "environment": {...},
  "simulation": {...},
  "exposure": {...},
  "risk": {...},
  "deployment": {...},
  "damage_control": {...},
  "explanation": {...}
}
```

Based on the authoritative `SpillAssessmentResult` contract. 

---

# 📊 Evaluation Metrics

The system evaluates:

* spread stability consistency
* risk ranking robustness
* runtime efficiency
* response allocation effectiveness

---

# ⚠️ Prototype Limitations

IOS-RPMP is:

✔ Physics-inspired
✔ Explainable
✔ Simulation-driven
✔ Real-geography based
✔ Laptop-runnable

But NOT:

* satellite-integrated
* military-grade ocean modeling
* real-time maritime authority connected
* production-scale ocean physics simulation

The system is intentionally positioned as:

> A marine emergency decision-support prototype — not a perfect ocean physics engine.

---

# 🔮 Future Enhancements

Planned upgrades:

* satellite integration
* real-time ocean current APIs
* AI-based severity prediction
* autonomous drone validation
* live ship tracking
* global coordination network
* advanced environmental datasets

---

# 🏆 Project Classification

IOS-RPMP combines:

* Scientific Simulation
* AI-Assisted Prediction
* Geospatial Intelligence
* Environmental Analytics
* Marine Protection Systems
* Decision Support Engineering

---

# 👨‍💻 Author

## Parvatham Bhavanarushi

---

# 📜 License

MIT License

---

# 🌊 Final Statement

IOS-RPMP demonstrates how environmental intelligence systems can combine:

* scientific simulation
* ecological risk analysis
* geospatial reasoning
* operational logistics
* explainable AI concepts

to improve marine disaster preparedness and ecosystem protection.

---

# ⭐ IOS-RPMP

> Predict. Prioritize. Protect.
