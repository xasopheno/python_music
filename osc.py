from __future__ import division
from math import pi
import numpy as np
import random
# import matplotlib.pyplot as plt


class SineOsc:
    def __init__(self):
        self.sample_rate = 44100

    def wave(self, frequency, length, rate):
        """produces sine across np array"""

        length = int(length * rate)
        factor = float(frequency) * (pi * 2) / rate
        waveform = np.sin(np.arange(length) * factor)

        return waveform

    def play_frequencies(self, stream, length, volume, attack, decay, *freqs):
        """Plays a group of frequencies"""

        def _create_waveform(freq):
            wave = [self.wave(freq, length, self.sample_rate)]
            waveform = (np.concatenate(wave) * volume / 16)

            fade_in = np.arange(0., 1., 1./attack)
            fade_out = np.arange(1., 0., -1./decay)

            waveform[:attack] = np.multiply(waveform[:attack], fade_in)
            waveform[-decay:] = np.multiply(waveform[-decay:], fade_out)

            return waveform

        all_tones = map(_create_waveform, freqs)
        all_tones = sum(all_tones)

        # plt.plot(chunk[])
        # plt.show()

        return stream.write(all_tones.astype(np.float32).tostring())
