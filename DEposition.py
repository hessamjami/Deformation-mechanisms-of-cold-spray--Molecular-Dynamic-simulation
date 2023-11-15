from pymatgen.io.lammps.data import LammpsData
from pymatgen.io.lammps.inputs import LammpsInput

# Create LammpsData object
box = LammpsData.box(0, 5, 0, 5, 0, 10)
data = LammpsData(lattice=LammpsData.lattice(fcc=1.0), box=box, units="lj")

# Add substrate atoms
data.add_atoms([{"type": 1, "x": 0, "y": 0, "z": 3}])

# Set pair style and coefficients
data.pair_style = "lj/cut"
data.pair_coeff = ["* * 1.0 1.0", "1 2 1.0 1.0 5.0"]

# Set bond style and coefficients
data.bond_style = "harmonic"
data.bond_coeff = ["1 5.0 1.0"]

# Set mass
data.mass = ["* 1.0"]

# Create group and region for mobile atoms
data.create_group("addatoms", "type 2")
data.create_region("mobile", "block 0 5 0 5 2 INF")
data.add_group_to_region("mobile", "addatoms")

# Create computes and fixes
data.create_compute("add", "addatoms temp")
data.modify_compute("add", "dynamic yes extra 0")
data.create_fix("1", "addatoms nve")
data.create_fix("2", "mobile langevin 0.1 0.1 0.1 587283")
data.create_fix("3", "mobile nve")

# Create molecule and fix for deposition
data.create_molecule("dimer", "molecule.dimer")
data.create_region("slab", "block 0 5 0 5 8 9")
data.create_fix("4", "addatoms deposit 100 0 100 12345 region slab near 1.0 mol dimer vz -1.0 -1.0")
data.create_fix("5", "addatoms wall/reflect zhi EDGE")

# Set thermo settings
data.thermo_style = "custom step atoms temp epair etotal press"
data.thermo = 100
data.modify_thermo("temp add lost/bond ignore lost warn")

# Run simulation
data.run(10000)

# Write Lammps input file
input_file = LammpsInput(data)
input_file.write_input("lammps_input.in")
