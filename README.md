# High-Performance Computing in Python

Welcome to my GitHub repository where I explore high-performance computing techniques in Python. This repository contains a series of Jupyter notebooks that demonstrate various methods to optimize and profile Python code for computational efficiency.

## Overview

The notebooks in this repository cover a range of topics including profiling Python code, optimizing with NumPy, leveraging Cython for compiling to C, and performing advanced matrix and vector computations.

## Notebooks

### 1. Benchmarking and Profiling
- `Benchmarking_and_Profiling1.ipynb`: Explores the use of decorators for timing functions, the `timeit` module for performance testing, and profiling tools like `cProfile`, `line_profiler`, and `memory_profiler`.

### 2. Lists and Tuples Optimization
- `List_and_Tuples.ipynb`: Demonstrates the time complexity differences between list and tuple operations, with a focus on append and delete actions.

### 3. Matrix and Vector Computations
- `Matrix_and_Vector_Computations.ipynb`: Investigates numerical simulations and performance optimizations using NumPy and NumExpr for matrix and vector operations.

### 4. Compiling Python to C with Cython
- `Compiling_to_c.ipynb`: Showcases the power of Cython to compile Python code to C for faster execution, complete with performance comparisons and visualizations.

## Key Functions and Classes

- `timefn`: A decorator for timing functions, ideal for quickly checking performance.
- `ParticleSimulator`: A class designed to simulate particle motion using both Python and NumPy techniques.
- `benchmark`: A function that tests and compares the performance of different code optimization strategies.
- `initialize_lattice`: Initializes a lattice for simulation in the Cython performance tests.
- `test_performance`: Measures the execution time of different update functions applied to the lattice.

## Visualizations

Performance comparisons are not just about numbers. Visualizations are provided to clearly illustrate the improvements gained through each optimization technique.

## Installation

To run these notebooks on your local machine, clone the repository, and ensure you have the following dependencies installed:

- Python 3.6+
- Jupyter Notebook
- NumPy
- Cython
- Matplotlib
- Pandas (for certain notebooks involving data analysis)
- Memory Profiler

## You can install most of the dependencies with:
pip install numpy cython matplotlib pandas memory_profiler jupyter
For Cython, you will need a C compiler set up on your machine.

## Usage
Each notebook is self-contained and includes comments that guide you through the steps performed for each optimization technique.

To run a notebook:
jupyter notebook <notebook_name>.ipynb

## Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your enhancements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
