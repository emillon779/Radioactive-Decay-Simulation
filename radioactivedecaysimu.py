import numpy as np
import matplotlib.pyplot as plt

# Parameters
N0 = 1000        # Initial number of nuclei
lambda_decay = 0.1  # Decay constant
total_time = 50  # Total simulation time
time_step = 0.1  # Time step for the simulation

# Time array
times = np.arange(0, total_time, time_step)

# Simulation
num_nuclei = np.zeros_like(times)
num_nuclei[0] = N0

for t in range(1, len(times)):
    decay_events = np.random.poisson(num_nuclei[t-1] * lambda_decay * time_step)
    num_nuclei[t] = num_nuclei[t-1] - decay_events
# Save the results to a file for Gnuplot
with open("decay_data.txt", "w") as f:
    for time, nuclei in zip(times, num_nuclei):
        f.write(f"{time}\t{nuclei}\n")

# Visualization using Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(times, num_nuclei, label="Simulated Data")
plt.title("Radioactive Decay Simulation")
plt.xlabel("Time")
plt.ylabel("Number of Nuclei")
plt.legend()
plt.grid(True)
plt.savefig("decay_curve.png")
plt.show()

print("Simulation completed and decay curve saved as decay_curve.png")
