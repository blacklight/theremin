import argparse
import sys

from .leap import list_leap_motions
from .sound import list_output_devices
from .sound.utils import midi_str_to_midi, midi_to_freq
from .theremin import theremin


def parse_args(args):
    parser = argparse.ArgumentParser(
            prog='theremin',
            description='Theremin emulator through a Leap Motion device.\n\n' +
            'Make sure that your Leap Motion device is plugged in and\n' +
            'the leapd daemon is running before running it.\n',
            epilog='\n------------\nAuthor: Fabio "BlackLight" Manganiello <blacklight86{a}gmail{d}com>\n',
            formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('--list-audio-outputs', '-l', dest='list_audio_outputs', required=False,
            action='store_true', help='List the available audio output devices')
    parser.add_argument('--list-leap-motions', '-L', dest='list_leap_motions', required=False,
            action='store_true', help='List the available Leap Motion devices')
    parser.add_argument('--audio-output', '-o', dest='audio_output', required=False,
            type=int, help='Select an output audio device by index (see -l)')
    parser.add_argument('--audio-backend', '-b', dest='audio_backend', required=False, default='portaudio',
            help='Select the audio backend (default: portaudio). Supported: ' +
            '{"portaudio", "jack", "coreaudio"}')
    parser.add_argument('--channels', '-c', dest='channels', required=False, type=int, default=2,
            help='Number of audio channels (default: 2)')
    parser.add_argument('--rate', '-r', dest='sampling_rate', required=False, type=int, default=44100,
            help='Sampling rate (default: 44100 Hz)')
    parser.add_argument('--discrete', '-d', dest='discrete', required=False, action='store_true',
            help='If set then discrete notes will be generated instead of samples over a continuous ' +
            'frequency space (default: false)')
    parser.add_argument('--left-handed', dest='left_handed', required=False, action='store_true',
            help='If set then the pitch control will be on the left hand and the volume control on the' +
            'right hand. Otherwise, the controls are inverted (default: false)')
    parser.add_argument('--generator', '-g', dest='generator', required=False,
            default='SineLoop', help='Wave generator to be used. See ' +
            'http://ajaxsoundstudio.com/pyodoc/api/classes/generators.html. ' +
            'Default: SineLoop')
    parser.add_argument('--min-frequency', dest='min_frequency', required=False, type=int, default=55,
            help='Minimum audio frequency (default: 55 Hz)')
    parser.add_argument('--max-frequency', dest='max_frequency', required=False, type=int, default=10000,
            help='Maximum audio frequency (default: 10 kHz)')
    parser.add_argument('--min-note', dest='min_note', required=False, type=str, default=None,
            help='Minimum MIDI note, as a string (e.g. A4)')
    parser.add_argument('--max-note', dest='max_note', required=False, type=str, default=None,
            help='Maximum MIDI note, as a string (e.g. A4)')

    opts, args = parser.parse_known_args(args)
    return opts, args


def main(args=None):
    if not args:
        args = sys.argv[1:]

    opts, args = parse_args(args)

    if opts.list_audio_outputs:
        list_output_devices()
        return

    if opts.list_leap_motions:
        list_leap_motions()
        return

    if opts.min_note:
        opts.min_frequency = midi_to_freq(midi_str_to_midi(opts.min_note))
    if opts.max_note:
        opts.max_frequency = midi_to_freq(midi_str_to_midi(opts.max_note))

    theremin(wave=opts.generator, audio_backend=opts.audio_backend, discrete=opts.discrete,
             min_frequency=opts.min_frequency, max_frequency=opts.max_frequency, left_handed=opts.left_handed,
             audio_output=opts.audio_output, channels=opts.channels, sampling_rate=opts.sampling_rate)
