import sys

import pyo

from .leap import LeapMotion
from .sound import SoundProcessor


def theremin(wave='SineLoop', audio_output=None, audio_backend='portaudio', channels=2,
             min_frequency=55, max_frequency=10000):
    dsp = SoundProcessor(output=audio_output, backend=audio_backend, channels=channels)
    dsp.start()

    assert hasattr(pyo, wave)
    wave = getattr(pyo, wave)
    audio = wave()
    channel = dsp.add_track(audio)
    print('Audio processor started')

    sensor = LeapMotion(dsp, track=channel, min_frequency=min_frequency, max_frequency=max_frequency)
    print('Press ENTER to quit')
    sys.stdin.readline()

    sensor.stop()
    dsp.shutdown()
