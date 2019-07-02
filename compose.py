from osc import SineOsc
import pyaudio
import random
import time
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), os.pardir))

sine_osc = SineOsc()

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=1,
                )


def idea(freq, length):
    freq /= 2
    rand = random.randrange(0, 20)
    if rand == 0:
        freq = 0
    sine_osc.play_frequencies(stream, length, .4, 500, 500,
                              freq / 2,
                              freq * random.choice([15/8, 0, 0, 0]) / 2,
                              freq * random.choice([3/2, 5/4, 7/4]),
                              freq * 5/2
                              )


if __name__ == '__main__':
    f = 440
    l = 0.15
    for iter in range(100):
        idea(f, l)
        idea(f * 3/2, l)
        idea(f * 5/4, l)
        l *= random.choice([0.5, 0.5, 0.25])
        if l < 0.1:
            l = 0.15
        if f > 1500:
            f = 140
        f *= random.choice([9/8, 7/8, 3/2, 9/8])

    idea(0, 2)
