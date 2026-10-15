from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

script_dir = Path(__file__).parent
csv_path = script_dir / "data.csv"

df = pd.read_csv(csv_path)
x = df["Distance (m)"].dropna()
y = df["Resistance"].dropna()

slope, intercept = np.polyfit(x, y, 1)
fig, ax = plt.subplots(figsize=(6, 4.5))

ax.scatter(
    x, y, 
    color="black", 
    facecolors="white", 
    edgecolors="black", 
    linewidths=0.8,
    label="Experimental Data ($N=50$)"
)

x_line = np.linspace(0.05, 0.55, 100)
y_line = slope * x_line + intercept
ax.plot(
    x_line, y_line, 
    color="black", 
    linestyle="--", 
    linewidth=1.0, 
    label=f"Linear Fit ($R = {slope:.1f}l + {intercept:.1f}$)"
)
ax.set_title("Resistance vs. Distance for Saltwater Bath")
ax.set_xlabel("Distance $l$ (m)")
ax.set_ylabel(r"Resistance $R$ ($\Omega$)")
ax.grid(True, linestyle=":", color="gray", alpha=0.6)
ax.legend(frameon=True, facecolor="white", edgecolor="black")

fig.tight_layout()
plt.show()
