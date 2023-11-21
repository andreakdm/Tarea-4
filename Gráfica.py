import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from scipy.optimize import fsolve

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(1, 19, 100)
y = ((9.81 * 68.1) / x) * (1 - np.e ** ((-1 * x * 10) / 68.1))

# plot
fig, ax = plt.subplots(figsize=(5, 5))

ax.plot(x, y, linewidth=2.0, label='Curva')
ax.set(xlim=(0, 19), xticks=np.arange(1, 19,2),
       ylim=(30, 81), yticks=np.arange(30, 81, 10)) 

# add horizontal line
ax.axhline(40, color='r', linestyle='--', label='y=40')

# find intersection
def eq(p):
    return (((9.81 * 68.1) / p) * (1 - np.e ** ((-1 * p * 10) / 68.1))) - 40

x_intersect = fsolve(eq, 0.1)
y_intersect = ((9.81 * 68.1) / x_intersect) * (1 - np.e ** ((-1 * x_intersect * 10) / 68.1))

# add vertical line
ax.axvline(x_intersect, color='r', linestyle='--', label='Intersección')

# add intersection point
ax.plot(x_intersect, y_intersect, 'ro')

plt.title("Velocidad vs coeficiente de resistencia", fontsize = 18)
plt.xlabel("Coeficiente de resistencia c", fontsize = 10)
plt.ylabel("Velocidad (m/s)", fontsize = 10)

# add legend with intersection point
ax.legend(title=f'Intersección: ({x_intersect[0]:.2f}, {y_intersect[0]:.2f})')

plt.show()
