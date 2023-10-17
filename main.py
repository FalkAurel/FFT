from logic import *
import math
import matplotlib.pyplot as plt
import numpy as np

temp = creatingEvenlySpacedNumbers(0, 2 * PI, 360)
func1 = [math.sin(number * 5) for number in temp] # creating 5hz wave
func2 = [math.sin(number * 7) for number in temp]# creating 7hz wave
func3 = [math.sin(number * 12) for number in temp]# creating 12hz wave
combinedFunc = [sum(wave) for wave in zip(func1, func2, func3)] #combining the waves

plt.plot(temp, func1, label="5hz")
plt.plot(temp, func2, label="7hz")
plt.plot(temp, func3, label="12hz")
plt.plot(temp, combinedFunc, label="combined")
plt.legend()
plt.show()

#creating test case
baseCase = np.array(temp)[:, None]
data = np.apply_along_axis(np.sin, 0, np.hstack((baseCase, baseCase, baseCase)) * np.array([5, 7, 12])).sum(axis=1)
plt.plot(baseCase.squeeze(), data)
plt.show()

myFFT = fft(padding(combinedFunc))
test = np.fft.fft(padding(data.tolist()))

print(np.allclose(myFFT, test))