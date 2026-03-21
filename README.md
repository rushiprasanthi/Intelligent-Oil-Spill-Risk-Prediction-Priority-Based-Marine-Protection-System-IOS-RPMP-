
# 🌊 IOS-RPMP  
## Intelligent Oil Spill Risk Prediction & Priority-Based Marine Protection System

---

## 🚀 Overview

IOS-RPMP is an AI-assisted, simulation-driven decision-support system designed to transform oil spill response from **reactive cleanup** to **predictive, prioritized protection**.

It integrates geospatial visualization, environmental simulation, ecological risk analysis, and deployment intelligence into a unified platform for marine emergency response.

---

## 🎯 Problem Statement

Oil spills spread rapidly across ocean surfaces, causing:

- Marine ecosystem destruction
- Coral reef damage
- Fish and bird mortality
- Economic losses (fisheries, tourism)

### Current Limitation:
Existing systems are **reactive**, acting only after damage occurs.

---

## 💡 Solution

IOS-RPMP provides:

✔ Real-time spill simulation  
✔ Dynamic risk scoring  
✔ Sensitive zone prioritization  
✔ Smart deployment recommendations  
✔ Decision-support outputs for authorities  

---

## 🧠 Core Features

### 🌍 1. Real-World Map Interaction
- Built with Leaflet.js
- Uses real geographic coordinates (OpenStreetMap)
- Right-click → simulate spill anywhere on Earth

---

### 🌊 2. Oil Spill Simulation Engine
- 2D grid-based advection–diffusion model
- Wind-driven directional spread
- Real-time animation

---

### 🟡 3. Sensitive Zone Intelligence
Predefined ecological zones:
- Coral reefs
- Mangroves
- Marine protected areas
- Fish breeding zones

Each zone includes:
- Sensitivity index (1–10)
- Economic impact weight

---

### 📊 4. Risk Scoring Engine

**Formula:**

```

Risk = (Sensitivity × Spread Speed × Exposure Probability) ÷ Time to Impact

```

Outputs:
- Risk score
- Priority level (P1 / P2 / P3)
- Impact ETA

---

### 🚢 5. Deployment Recommendation System

- Finds nearest port (O(n) algorithm)
- Calculates distance & ETA
- Suggests number of ships

**Rules:**
- High risk → 3 ships
- Medium → 2 ships
- Low → 1 ship

---

### 📉 6. Damage Control Estimation

```

Damage Controlled % = (1 - Exposure) × 100 ± timing adjustment

```

- Considers response timing
- Predicts containment effectiveness

---

### 📧 7. Alert System (Prototype)

Generates structured emergency alert:
- Spill location
- Priority zones
- Deployment plan
- ETA & recommendations

---

## 🧱 System Architecture

```

User Interaction (Map)
↓
Spill Event Trigger
↓
Simulation Engine
↓
Exposure Calculation
↓
Risk & Priority Engine
↓
Deployment Logic
↓
Damage Estimation
↓
Dashboard + API Output

````

---

## 🛠️ Tech Stack

### Frontend
- HTML, CSS, JavaScript
- Leaflet.js

### Backend
- Python (FastAPI)

### Simulation
- NumPy

### Database (Optional)
- PostgreSQL + PostGIS

### ML (Future Scope)
- Scikit-learn
- TensorFlow

---

## 📦 API Endpoint

### POST `/simulate_spill`

#### Response:
```json
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
````

---

## 🖥️ UI Features

* 🌍 Interactive map
* 🌊 Animated spill spread
* 🟡 Highlighted sensitive zones
* 📊 Real-time dashboard
* 🌬 Wind direction indicator
* 🚢 Ship deployment visualization

---

## 📈 Evaluation Metrics

* Spread stability consistency
* Priority ranking robustness
* Simulation runtime efficiency
* Response allocation efficiency

---

## ⚠️ Limitations

* Not real-time satellite-based
* Simplified ocean physics
* Static datasets (prototype)
* No live maritime integration

---

## 🔮 Future Enhancements

* Satellite data integration
* AI-based prediction models
* Real-time ocean current APIs
* Drone validation systems
* Global coordination layer

---

## 🏆 Project Type

Hybrid System:

* Scientific Simulation
* AI-Enhanced Prediction
* Decision Intelligence Platform
* Web-Based Visualization Tool

---

## 🎯 Conclusion

IOS-RPMP is a **marine environmental defense intelligence system** that combines:

* Physics-based simulation
* AI-assisted prediction
* Risk prioritization
* Operational decision support

> Designed as a **decision-support prototype**, not a perfect ocean physics model.

---

## 👨‍💻 Author

parvatham bhavanarushi

---

**

Just tell me 👍
```
