import numpy as np
import matplotlib.pyplot as plt

# a) Find R, lambda_D, and z
R = 63  # [m]
lambda_D = 7.55  # [-]
z = 3  # [-]

# b) Find optimal AoA and cL
# Import Airfoil file
AirfoilFile = r'IntrodutionToWindTurbineAerodynamics\01_Exercise_Basic_Blade_Design\Solution\IEA-15-240-RWT_AeroDyn15_Polar_36.dat'
AirfoilData = np.loadtxt(AirfoilFile, skiprows=54)

AoA = AirfoilData[:, 0]
Cl = AirfoilData[:, 1]
Cd = AirfoilData[:, 2]
Cm = AirfoilData[:, 3]

# Calculate lift-to-drag ratio
epsilon = Cl / Cd

# Find maximum value
MaxIdx = np.argmax(epsilon)
MaxVal = epsilon[MaxIdx]

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
AeroFile = r'IntrodutionToWindTurbineAerodynamics\01_Exercise_Basic_Blade_Design\Material\NRELOffshrBsline5MW_AeroDyn_Equil_noTwr.dat'
NodeData = np.loadtxt(AeroFile, skiprows=26, usecols=(0, 1, 2, 3, 4))

RNodes = NodeData[:, 0]
AeroTwst = NodeData[:, 1]
DRNodes = NodeData[:, 2]
Chord = NodeData[:, 3]
NFoil = NodeData[:, 4]

# Missing design parameters
alpha_A = AoA[MaxIdx]  # [deg]
c_L = Cl[MaxIdx]  # [-]

# Calculate twist angle
r = RNodes
beta = np.degrees(np.arctan((2/3) * R / lambda_D / r)) - alpha_A
c = (1 / z) * (8/9) * (2 * np.pi * R / c_L) * (1 / (lambda_D * np.sqrt((lambda_D * r / R) ** 2 + 4/9)))

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