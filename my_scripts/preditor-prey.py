# preditor-prey.py
# modified from https://github.com/mikesaint-antoine/Comp_Bio_Tutorials
# see Youtube video at: https://www.youtube.com/watch?v=2f5aRTBmm10

import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Initial values.
y0 = [10,1] # [fish, bears] units in hundreds

t = np.linspace(0,50,num=1000)

alpha = 1.1 # Fish birth rate
beta = 0.4  # Fish death rate
delta = 0.1 # Bear birth rate
gamma = 0.4 # Bear death rate

# steady state initial conditions (uncomment to overwrite y0 above).
# y0 = [gamma/delta , alpha/beta] # [fish, bears] units in hundreds

# Create list of all model parameters.
params = [alpha, beta, delta, gamma]

# Define simulation function.
def sim(variables, t, params):

    # fish population level
    x = variables[0]

    # bear population level
    y = variables[1]


    alpha = params[0]
    beta = params[1]
    delta = params[2]
    gamma = params[3]

    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y

    return([dxdt, dydt])

# Simulate with ODE.
y = odeint(sim, y0, t, args=(params,))

# Plot the results.
fig, ax = plt.subplots()

line1, = ax.plot(t, y[:,0], color="b", label="Fish")
line2, = ax.plot(t, y[:,1], color="r", label="Bears")

ax.set_ylabel("Population (hundreds)")
ax.set_xlabel("Time")
ax.legend()

plt.show()
