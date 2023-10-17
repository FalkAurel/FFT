# FFT Implementation in Vanilla Python

This repository contains an implementation of the Fast Fourier Transform (FFT) using the Cooley-Tukey radix-2 Decimation in Time (DIT) algorithm, written in pure Python without the use of external libraries.

## Contents

The code includes the following functions:

- `creatingEvenlySpacedNumbers(start, end, nPoints)`: Generates a list of evenly spaced numbers between a start and end point.
- `exp(X, *, precision=100)`: Approximates the exponential function using a Taylor series.
- `padding(data)`: Pads the input data with zeros until the length of the data is a power of two.
- `fft(data)`: Applies the Cooley-Tukey radix-2 DIT algorithm to compute the FFT of the input data.

## Usage

The main function to use is `fft(data)`, which takes a list of real numbers as input and returns their FFT as a list of complex numbers. The input list length should be a power of two. If it's not, you can use the `padding(data)` function to pad your data with zeros until its length is a power of two. By applying the FFT, you can extract the frequencies which make up the signal.
![ima](https://github.com/FalkAurel/FFT/assets/137809006/6fba60b0-496e-4f86-a746-bd4b6645f09e)

## Note

This implementation is intended for educational purposes and may not be as efficient as FFT implementations in numerical libraries like NumPy or SciPy. It demonstrates the underlying mathematical concepts and provides a basis for understanding how FFT algorithms work.
