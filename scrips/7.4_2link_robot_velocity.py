# 7.4 - 2 link planar robot velocity ellipse

import numpy as np
import roboticstoolbox as rtb

import matplotlib.pyplot as plt

# Create the model
p2 = rtb.models.DH.Planar2()

# Assign some angles
p2.q = [0.1, 0.2]

# Plot and include the Velocity Ellipsoid
#p2.plot(p2.q, vellipse=True)

from roboticstoolbox import ETS as ets
# Links 
a1=1
a2=1

# Angles
q1=0
q2 = np.pi/2

e = ets.rz(q1)*ets.tx(a1)*ets.rz(q2)*ets.tx(a2)
print(e.eval( [q1, q2] ))
e.plot([q1,q2],vellipse=True)
