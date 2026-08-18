import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Symmetric example data
x_train = np.array([0, 1, 2])
y_train = np.array([0, 2, 4])  # Perfectly linear, y = 2x + 0

def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost_sum = 0
    for i in range(m):
        f_wb = w * x[i] + b
        cost = (f_wb - y[i]) ** 2
        cost_sum += cost
    return (1 / (2 * m)) * cost_sum

# Create grid of w and b values
w_vals = np.linspace(0, 4, 50)  # centered around true w=2
b_vals = np.linspace(-2, 2, 50) # centered around true b=0
W, B = np.meshgrid(w_vals, b_vals)

# Compute cost for each (w,b)
Z = np.zeros_like(W)
for i in range(W.shape[0]):
    for j in range(W.shape[1]):
        Z[i,j] = compute_cost(x_train, y_train, W[i,j], B[i,j])

# Plotting
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(W, B, Z, cmap='viridis', alpha=0.8)
ax.set_xlabel('Weight (w)')
ax.set_ylabel('Bias (b)')
ax.set_zlabel('Cost J(w,b)')
ax.set_title('Symmetric Cost function surface: w vs b vs Cost')
plt.show()
