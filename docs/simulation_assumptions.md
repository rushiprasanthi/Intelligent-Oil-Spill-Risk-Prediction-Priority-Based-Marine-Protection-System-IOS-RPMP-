# Simulation Assumptions & Limitations

## Purpose
The simulation engine is designed to approximate oil spill spread behavior
for rapid decision-support, not for precise physical prediction.

---

## Core Assumptions

1. **2D Surface Spread**
   - Oil is modeled as a surface phenomenon
   - Vertical mixing is ignored

2. **Uniform Grid**
   - Fixed grid resolution
   - No bathymetry or shoreline interaction

3. **Constant Wind**
   - Wind speed and direction are constant during a run
   - No stochastic weather variation

4. **Simplified Diffusion**
   - Diffusion approximates lateral spreading
   - Not a Navier–Stokes solver

5. **Time-Stepped Growth**
   - Spread evolves in discrete hourly steps
   - Suitable for emergency planning timescales

---

## Why These Assumptions Are Acceptable

- Enables laptop execution
- Allows explainable behavior
- Suitable for early-stage response decisions
- Common in first-order environmental modeling

---

## Explicit Non-Goals

- Exact shoreline contamination prediction
- Chemical weathering modeling
- Satellite image assimilation
