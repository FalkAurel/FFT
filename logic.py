PI = 3.141592653589793

def creatingEvenlySpacedNumbers(start, end, nPoints):
    distanceBetweenPoints = (end - start) / (nPoints - 1)
    return [start + currentNumber * distanceBetweenPoints for currentNumber in range(nPoints)]

def exp(X, *, precision=100):
    """
    Returns the exp function by approximating it with a taylor series. Where the formula is
    sum(1 + x**n / n!) where n goes to infinity.
    """
    def factorial(n):
        """
        Returns n!.
        """
        if n < 2:
            return 1
        output = 1
        for number in range(2, n + 1):
            output *= number
        return output
    return sum([(X)**exponent / factorial(exponent) for exponent in range(precision)])

def padding(data):
    nSamples = len(data)
    if  nSamples & (nSamples - 1) == 0 and nSamples != 0:
        return data
    nextPowerOfTwo = 1 << (len(bin(nSamples)) - 2)
    difference = nextPowerOfTwo - nSamples
    return data + [0 for _ in range(difference)]

def fft(data):
    """
    Applying the Cooley-Tukey radix-2 Decimation in Time (DIT) algorithm.
    """
    nSample = len(data)
    if nSample < 2:
        return data
    even, odd = fft(data[0::2]), fft(data[1::2])
    weight = [exp(-2j* PI * index / nSample) * odd[index] for index in range(nSample // 2)]
    return [even[index] + weight[index] for index in range(nSample // 2)] + [even[index] - weight[index] for index in range(nSample // 2)]
