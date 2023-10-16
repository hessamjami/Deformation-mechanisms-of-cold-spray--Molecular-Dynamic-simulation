# Deformation-mechanisms-of-cold-spray--Molecular-Dynamic-simulation
This simulation focuses on titanium nanoparticles, unveiling insights into deformation, stresses, and temperatures during impact. Join us in the world of ultrafast deformation and amorphous state transformations.  Discover the atomic secrets of Cold Spray!
# Molecular Dynamics Simulation of Titanium Nanoparticles Deposition

This repository contains C++ code for conducting molecular dynamics simulations of titanium nanoparticles deposition on a titanium substrate using LAMMPS. The code allows you to study local stress, temperature, and particle deformation behavior during impact.

## Getting Started

Before running the code, you need to prepare the atomic structure of particles and the substrate, and specify the potential file for your material. You can follow these steps:

### Prepare Atomic Structures:

1. Use molecular modeling software like ArgusLab or Avogadro to create atomic structures for your particles and substrate.
2. Save the atomic structure data in a file (e.g., data.txt) in a format suitable for LAMMPS.

### Potential File:

1. Choose the potential file for your material. In this example, we used the eam/fs potential for titanium.
2. You can download the potential file for titanium from NIST.

### Compile and Run the Code:

1. Clone this repository to your local machine.
2. Build the code with a C++ compiler (e.g., g++).
3. Run it with the LAMMPS executable using the following command:

```shell
lmp_mpi -in in.txt
Make sure to specify the paths to the atomic structure data and potential file in your LAMMPS input script (in.txt) when running the code.

Dependencies
LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator)
C++ Compiler (e.g., g++)
Usage
After setting up the atomic structure and potential file, you can run the code using LAMMPS as described above.
## References
- Jami, H., & Jabbarzadeh, A. (2019). Unraveling ultrafast deformation mechanisms in surface deposition of titanium nanoparticles. *Applied Surface Science*, 489, 446-461.

