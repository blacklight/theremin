import argparse
import sys

from . import theremin
from .leap import list_leap_motions
from .sound import list_output_devices


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--list-audio-outputs', '-l', dest='list_audio_outputs', required=False,
                        action='store_true', help='List the available audio output devices')
    parser.add_argument('--list-leap-motions', '-L', dest='list_leap_motions', required=False,
                        action='store_true', help='List the available Leap Motion devices')
    parser.add_argument('--audio-output', '-o', dest='audio_output', required=False,
                        type=int, help='Select an output audio device by index (see -l)')
    parser.add_argument('--audio-backend', '-a', dest='audio_backend', required=False, default='portaudio',
                        help='Select the audio backend (default: portaudio). Supported: ' +
                             '{"portaudio", "jack", "coreaudio"}')
    parser.add_argument('--channels', '-c', dest='channels', required=False, type=int, default=2,
                        help='Number of audio channels (default: 2)')
    parser.add_argument('--generator', '-g', dest='generator', required=False,
                        default='SineLoop', help='Wave generator to be used. See ' +
                        'http://ajaxsoundstudio.com/pyodoc/api/classes/generators.html. ' +
                        'Default: SineLoop')
    parser.add_argument('--min-frequency', '-m', dest='min_frequency', required=False, type=int, default=55,
                        help='Minimum audio frequency (default: 55 Hz)')
    parser.add_argument('--max-frequency', '-M', dest='max_frequency', required=False, type=int, default=10000,
                        help='Maximum audio frequency (default: 10 kHz)')

    opts, args = parser.parse_known_args(args)
    return opts, args


def main(args):
    opts, args = parse_args(args)

    if opts.list_audio_outputs:
        list_output_devices()
        return

    if opts.list_leap_motions:
        list_leap_motions()
        return

    theremin(wave=opts.generator, audio_backend=opts.audio_backend,
             min_frequency=opts.min_frequency, max_frequency=opts.max_frequency,
             audio_output=opts.audio_output, channels=opts.channels)


if __name__ == "__main__":
    main(sys.argv[1:])
