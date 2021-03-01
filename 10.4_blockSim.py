import bdsim
from bdsim.blocks.transfers import Integrator

## Lecture 10.4

# In this notebook, we will learn to model a dynamical system using the bdsim simulation class.  
# Learn more at:\
# https://petercorke.github.io/bdsim/

# We will begin by modeling the mass-spring system which resembles the behvior of motors and thus it is appropriate to understand for robotics.

# First create a bdsim object instance
bd = bdsim.BlockDiagram(None)

# After that, create all necessary objects used in the dynamical system.
# define the blocks
demand = bd.STEP(T=1, pos=(0,0), name='demand') # input step signal

sum    = bd.SUM('+-', pos=(1,  0))              # addition operation

minv   = bd.GAIN( 0.5,  pos=(1, 2))            # 1/m gain
b      = bd.GAIN(-2.0,  pos=(2, 0))            # -b gain
k      = bd.GAIN(-10.0, pos=(3, -1))           # -K gain

int1 = bd.add_block(Integrator, name = "xdd2xd")
int2 = bd.add_block(Integrator, name = "xd2x")

scope = bd.SCOPE(name='x', styles=['k', 'r--'], pos=(6,2))

### Connections
# In bdsim all wires are point to point, a one-to-many connection is implemented by many wires.

# **Ports**\
# Ports are designated using Python indexing and slicing notation, for example sum[0]. 
# 
# **Input or Output**:\
# Whether a port is an input or output port depends on context.
# 
# Blocks are connected by `connect(from, to_1, to_2, ...)`.
# 
# So an index on: 
# - the first argument refers to an output port, 
# - the second (or subsequent) arguments refers to an input port. 
# 
# If a port has only a single port then no index is required.

# **Bundle of wires**:\
# Can be denoted using slice notation, for example block[2:4] refers to ports 2 and 3. 
# 
# When connecting slices of ports the number of wires in each slice must be consistent. 
# 
# You could even do a cross over by connecting block1[2:4] to block2[5:2:-1].

# Connect the blocks
bd.connect(demand, sum[0], scope[1])    # desired incoming position

bd.connect(sum, minv)
bd.connect(minv, int1)

bd.connect(int1, b)
bd.connect(int1, int2)

bd.connect(int2, scope)
bd.connect(int2, k)


# ### Checking:
# Before running, it is important to ensure that the diagram has been correctly constructed. To that end, we can use the compile() method.
# Checks
bd.compile()   # check the diagram

# ### Reporting:
# It is possible to obtain a report of the block diagram by using the report() method. This will show the numa of the blocks, their inputs, outputs, and state, along with wire connection information.
bd.report()    # list all blocks and wires


# ### Simulating:
# Once you are sure your model is correct, you can simulate the behavior of the simulated model according to the desired input. Normally, if you have modelled your plant well, it will closely track whatever input signal you have sent to it.
# 
# You can think of this is as your robot joints following the precise joint angles that you have input to it from jtraj() or some similar method.
# 
# Currently the run method uses a variable-step Rk45 solver by default and saves output values at least every 0.1s. 
# 
# ### Visualization:
# fter running the simulation, we want to study the output of the plant. The run() method will generate data graphs automatically. 

# Run 
bd.run(5)             # simulate for 5s
#bd.run(5, dt=0.01)   # You can alternatively adjust the dt variable


# ### Saving the Visualization 
# If you wish to save the graphs, you can save them localy into a graphviz or pdf format as shown below.
# 
# PDFs are simple:
bd.savefig('pdf')      # save all figures as pdf

# If you choose to save them into a graphviz format with the bd.dotfile() method, you will need to use either:
# - the 'dot' program, or 
# - the 'neato' program 
# 
# In linux to visualize. 
bd.dotfile('bd1.dot')  # output a graphviz dot file

# Then in a bash terminal outside of the python interpreter do:
# dot -Tpng -o demo.png demo.dot
# neato -Tpng -o demo.png demo.dot


# Display characteristics:
# - Sources:   3D boxes
# - Sinks:     folders
# - Gains:     triangles
# - Summing:   points
# - Functions: boxes
# - Transfer Functions: connectors that look likegates

bd.done()

