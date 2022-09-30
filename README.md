# RNG-and-number-primality
This is a project that provides two algorithms for random number generation (Lagged Fibonacci Generator and Linear Congruential Generator) and two algorithms for number primality test (Miller Rabin and Fermat).

## Development Environment
Language: Python 3.10.4

Machine: Ubuntu 22.04.1

## How to run
The project has a Makefile. The steps to run are displayed below.

### 1. Install dependencies
This project requires the Python language installed and ready to use. Beside that, to install the project local dependencies run:

```
make dependencies
```

### 2. Environment setup
The project requires the instalation of some python packages. It is recommended to install the packages in a virtual environment. Both the virtual environment creation and the packages instalation can be done running:
```
make setup
```

### 3. Running tests
To run the random number generation test execute:
```
make testrng
```

To run the prime number generation test execute:

```
make testprime
```
NOTE: this test can take couple hours depending on the hardware. Modify the test script (specially how many runs it will execute) if needed.

### 4. Plotting results
To plot random number generation results execute:
```
make plotrng
```

To plot prime number generation results execute:
```
make plotprime
```

### 5. Cleaning workspace
To clean the workspace, run:
```
make clean
```
It will remove the virtual environment and python cached files

## Output
The results are stored in the output folder. CSV files store tests results and PDF files are the plot figures
