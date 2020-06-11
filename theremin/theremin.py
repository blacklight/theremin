import sys
import pyo

from .leap import LeapMotion
from .sound import SoundProcessor


def theremin(wave='SineLoop', audio_output=None, audio_backend='portaudio', channels=2, min_frequency=55,
             max_frequency=10000, sampling_rate=44100, discrete=False, left_handed=False):
    dsp = SoundProcessor(output=audio_output, backend=audio_backend, channels=channels, sampling_rate=sampling_rate, discrete=discrete)
    dsp.start()

    assert hasattr(pyo, wave)
    wave = getattr(pyo, wave)
    audio = wave()
    channel = dsp.add_track(audio)
    print('Audio processor started')

    sensor = LeapMotion(dsp, track=channel, min_frequency=min_frequency, max_frequency=max_frequency,
                        left_handed=left_handed)
    print('Press ENTER to quit')
    sys.stdin.readline()

    sensor.stop()
    dsp.shutdown()
