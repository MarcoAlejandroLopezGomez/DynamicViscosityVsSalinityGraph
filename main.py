import matplotlib.pyplot as plt
import numpy as np

# 1. Independent Variable: NaCl Concentration (g/dm^3)
x = np.array([0, 50, 75, 125, 150])

# 2. Dependent Variable: Mean Dynamic Viscosity (Pa*s) 
# Values averaged from your 25 trials in the provided images
y = np.array([0.2893105919, 0.3400506183, 0.3457887432, 0.3380097867, 0.3333006271])

# 3. Absolute Uncertainties (Pa*s)
# Averaged from the 'absolute uncertainty' column in your spreadsheet
y_err = np.array([0.08912386717, 0.1171794708, 0.1104416189, 0.1085220822, 0.09896255668])

# 4. Instrumental uncertainty for Concentration (from your balance)
x_err = 0.05 

# Set up the plot
plt.figure(figsize=(10, 7))
plt.style.use('seaborn-v0_8-whitegrid')

# Create the scatter plot with unique error bars for each data point
plt.errorbar(x, y, yerr=y_err, xerr=x_err, fmt='o', color='navy', 
             ecolor='black', capsize=4, elinewidth=1, markeredgewidth=1, 
             label='Experimental Data ($\eta \pm \Delta \eta$)')

# Calculate the linear regression for the best fit line [1]
slope, intercept = np.polyfit(x, y, 1)
plt.plot(x, slope*x + intercept, color='red', linestyle='--', 
         label=f'Best Fit Line: $y = {slope:.5f}x + {intercept:.4f}$')

# 5. Formal labels and titles with units
plt.title('Graph 1: Dynamic Viscosity ($\eta$) vs. Sodium Chloride Concentration', fontsize=14)
plt.xlabel('NaCl Concentration ($g/dm^3$)', fontsize=12)
plt.ylabel('Dynamic Viscosity ($Pa \cdot s$)', fontsize=12)
plt.legend(frameon=True)

# Add annotations for the gradient and intercept to satisfy reporting rules
plt.text(10, 0.45, f'Gradient (m): {slope:.5f} $Pa \cdot s / (g \cdot dm^{{-3}})$ \nIntercept (c): {intercept:.4f} $Pa \cdot s$', 
         bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()
plt.show()