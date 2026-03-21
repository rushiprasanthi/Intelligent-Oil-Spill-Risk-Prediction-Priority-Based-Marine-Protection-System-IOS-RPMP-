# IOS-RPMP System Architecture

## Overview
IOS-RPMP (Intelligent Oil Spill Risk Prediction & Priority-Based Marine Protection System)
is a decision-support prototype designed to assist marine authorities during oil spill incidents.

The system is not a full ocean physics model. It is a lightweight, explainable,
laptop-runnable prototype focused on decision prioritization.

---

## Architectural Layers

### 1. Frontend Layer
- Leaflet-based interactive map
- User initiates spill events via right-click
- Displays priority, risk score, exposure, port, ETA, and explanation

### 2. Backend API Layer
- FastAPI-based REST service
- Orchestrates simulation, risk analysis, and deployment logic
- Stateless and modular

### 3. Simulation Layer
- 2D grid-based spread model
- Advection–diffusion inspired
- Wind-driven directional spread
- Time-stepped growth

### 4. Decision Logic Layer
- Classical environmental risk modeling
- Base hazard + zone impact
- No AI / No ML
- Fully explainable formulas

### 5. Deployment Intelligence
- Nearest port selection
- ETA estimation
- Rule-based ship allocation

---

## Key Design Principles

- Explainability over black-box intelligence
- Deterministic behavior
- Configurable parameters
- Demo-safe and judge-friendly

---

## System Disclaimer
This system is a decision-support prototype and does not replace
high-resolution hydrodynamic or satellite-driven spill models.
