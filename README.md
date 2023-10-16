# Deformation-mechanisms-of-cold-spray--Molecular-Dynamic-simulation
This simulation focuses on titanium nanoparticles, unveiling insights into deformation, stresses, and temperatures during impact. Join us in the world of ultrafast deformation and amorphous state transformations.  Discover the atomic secrets of Cold Spray!
# Molecular Dynamics Simulation of Titanium Nanoparticles Deposition

This repository contains C++ code for conducting molecular dynamics simulations of titanium nanoparticles deposition on a titanium substrate using LAMMPS. The code allows you to study local stress, temperature, and particle deformation behavior during impact.

## Getting Started

Before running the code, you need to prepare the atomic structure of particles and the substrate, and specify the potential file for your material. You can follow these steps:

1. **Prepare Atomic Structures:**
   - Use molecular modeling software like ArgusLab or Avogadro to create atomic structures for your particles and substrate.
   - Save the atomic structure data in a file (e.g., `data.txt`) in a format suitable for LAMMPS.

2. **Potential File:**
   - Choose the potential file for your material. In this example, we used the eam/fs potential for titanium.
   - You can download the potential file for titanium from [NIST](https://www.ctcms.nist.gov/potentials/testing/system/Ti/).

3. **Compile and Run the Code:**
   - Clone this repository to your local machine.
   - Build the code with a C++ compiler (e.g., g++) and run it with the LAMMPS executable.
   - You'll need to specify the paths to the atomic structure data and potential file when running the code.

## Dependencies

- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator)
- C++ Compiler (e.g., g++)

## Usage

After setting up the atomic structure and potential file, you can run the code using LAMMPS as follows:

```bash
lammps -i in.txt
