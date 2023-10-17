from logic import PI, exp

def discreteFourierTransform(signal):
    nSamples = len(signal)
    zeta = exp(-2j * PI / nSamples)
    preComputedZeta = [zeta **zetaPower for zetaPower in range(nSamples)]
    return [sum([signal[sample] * preComputedZeta[(frequency * sample) % nSamples] for sample in range(nSamples)]) for frequency in range(nSamples)]