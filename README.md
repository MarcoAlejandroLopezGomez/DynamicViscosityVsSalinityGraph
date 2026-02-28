# Dynamic Viscosity vs Salinity Graph

## Purpose
This project generates a graph for my **IB Physics SL Internal Assessment (IA)**.

In short, it is used to show and analyze how the **dynamic viscosity** of a solution changes as **NaCl concentration (salinity)** increases.

## What this code does
- Plots experimental data points of viscosity vs concentration.
- Adds **error bars** for both variables (uncertainties).
- Calculates and draws a **linear best-fit line**.
- Displays the **gradient** and **intercept** on the graph.

## Tools and libraries used
- **Python**
- **NumPy**: arrays and linear regression (`polyfit`)
- **Matplotlib**: graph creation, error bars, labels, and annotations

## Variables used in the graph
- **Independent variable (x):** NaCl concentration \(g/dm^3\)
- **Dependent variable (y):** Mean dynamic viscosity \(Pa·s\)
- **Uncertainty in viscosity:** absolute uncertainty for each data point
- **Uncertainty in concentration:** instrumental uncertainty from balance

## How to run
1. Install dependencies:
   - `pip install numpy matplotlib`
2. Run:
   - `python main.py`

The script will open the final IA graph window.
