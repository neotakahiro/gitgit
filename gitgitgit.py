import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Constants
Lx, Ly = 1, 1  # Domain dimensions (m)
Nx, Ny = 100, 100  # Number of grid points
dx, dy = Lx / (Nx - 1), Ly / (Ny - 1)  # Grid spacing (m)
total_time = 12.0  # Total simulation time (s)
thermal_diffusivities = [0.5 * 1e-4, 1e-4, 1.5 * 1e-4]  # Different thermal diffusivities

def init_temperature_field(Nx, Ny):
    T = np.zeros((Ny, Nx))
    T[Ny // 2 - 10 : Ny // 2 + 10, Nx // 2 - 10 : Nx // 2 + 10] = 100
    return T

def update_temperature(T, alpha, dt, dx, dy):
    T_new = T.copy()
    T_new[1:-1, 1:-1] = (
        T[1:-1, 1:-1]
        + alpha * dt * (
            (T[1:-1, 2:] - 2 * T[1:-1, 1:-1] + T[1:-1, :-2]) / dx**2
            + (T[2:, 1:-1] - 2 * T[1:-1, 1:-1] + T[:-2, 1:-1]) / dy**2
        )
    )
    return T_new

fig, axes = plt.subplots(3, 2, figsize=(12, 12), sharex='col', sharey='row')

for i, alpha in enumerate(thermal_diffusivities):
    dt = 0.25 * min(dx, dy)**2 / alpha  # Time step (s)
    T = init_temperature_field(Nx, Ny)
    n_steps = int(total_time / dt)
    
    for step in range(n_steps + 1):
        T = update_temperature(T, alpha, dt, dx, dy)

    # Plot the final temperature distribution in the xy-plane
    im = axes[i, 0].imshow(T, cmap='hot', origin='lower', extent=[0, Nx, 0, Ny])
    axes[i, 0].set_title(f'Temperature Distribution (α = {alpha:.1e})')
    axes[i, 0].set_ylabel('y (m)')

    # Create a custom colorbar axis with the same length as the y-axis
    divider = make_axes_locatable(axes[i, 0])
    cax = divider.append_axes("right", size="5%", pad=0.1)
    fig.colorbar(im, cax=cax, label='Temperature (°C)')

    # Plot the temperature profile along the x-axis through the center
    x = np.linspace(0, Lx, Nx)
    axes[i, 1].plot(x, T[Ny // 2, :], label=f'α = {alpha:.1e}')
    axes[i, 1].set_title(f'Temperature Profile (α = {alpha:.1e})')
    axes[i, 1].set_ylabel('Temperature (°C)')

# Set the x-axis label for the bottom subplots
for ax in axes[-1, :]:
    ax.set_xlabel('x (m)')

plt.suptitle('2D Heat Transfer for Different Thermal Diffusivities')
plt.tight_layout(rect=[0.1, 0.03, 1, 0.95])  # Increase left margin to 0.1
plt.show()
