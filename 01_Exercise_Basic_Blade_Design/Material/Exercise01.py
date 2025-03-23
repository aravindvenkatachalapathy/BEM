import numpy as np
import matplotlib.pyplot as plt

# a) Find R, lambda_D, and z
R = np.nan              # [m]
lambda_D = np.nan     # [-]
z = np.nan               # [-]

# b) Find optimal AoA and cL
# Import Airfoil file
AirfoilFile = 'NACA64_A17.dat'
AirfoilData = np.loadtxt(AirfoilFile, skiprows=14)

AoA = AirfoilData[:, 0]
Cl = AirfoilData[:, 1]
Cd = AirfoilData[:, 2]
Cm = AirfoilData[:, 3]

# Calculate lift-to-drag ratio
epsilon = np.nan(np.size(AoA)) % please adjust

# Find maximum value


# Plot Lift and Drag
plt.figure()
plt.grid(True)
plt.box(True)
plt.plot(AoA, Cl, label='Lift')
plt.plot(AoA, Cd, label='Drag')
plt.xlabel(r'\alpha_{A} [deg]')
plt.ylabel(r'c_{L}, c_{D} [-]')
plt.legend()
plt.show()

# Plot lift-to-drag ratio
plt.figure()
plt.grid(True)
plt.box(True)
plt.plot(AoA, epsilon)
plt.xlabel(r'\alpha_{A} [deg]')
plt.ylabel(r'\epsilon [-]')
plt.show()

# c) Find twist and chord
# Import AeroDyn file
AeroFile = 'NRELOffshrBsline5MW_AeroDyn_Equil_noTwr.dat'
NodeData = np.loadtxt(AeroFile, skiprows=26, usecols=(0, 1, 2, 3, 4))

RNodes = NodeData[:, 0]
AeroTwst = NodeData[:, 1]
DRNodes = NodeData[:, 2]
Chord = NodeData[:, 3]
NFoil = NodeData[:, 4]

# Missing design parameters
alpha_A = np.nan  # [deg]
c_L = np.nan  # [-]

# Calculate twist angle
r = np.nan(np.size(RNodes))
beta = np.nan(np.size(RNodes))
c = np.nan(np.size(RNodes))

# d) Compare to NREL results
plt.figure()
plt.grid(True)
plt.box(True)
plt.plot(RNodes, beta, '.-', label='Betz')
plt.plot(RNodes, AeroTwst, 'o-', label='NREL')
plt.xlabel('r [m]')
plt.ylabel(r'\beta [deg]')
plt.title('Comparison Twist Angle')
plt.legend()
plt.show()

plt.figure()
plt.grid(True)
plt.box(True)
plt.plot(RNodes, c, '.-', label='Betz')
plt.plot(RNodes, Chord, 'o-', label='NREL')
plt.xlabel('r [m]')
plt.ylabel('c [m]')
plt.title('Comparison Chord Length')
plt.legend()
plt.show()
