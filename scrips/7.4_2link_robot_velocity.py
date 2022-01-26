# 7.4 - 2 link planar robot velocity ellipse

import numpy as np
import roboticstoolbox as rtb

import matplotlib.pyplot as plt

# Create the model
p2 = rtb.models.DH.Planar2()

# Assign some angles
p2.q = [0.1, 0.2]

# Plot and include the Velocity Ellipsoid
p2.plot(p2.q, vellipse=True)
