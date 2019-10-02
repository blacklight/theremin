# theremin

This is a [theremin](https://en.wikipedia.org/wiki/Theremin) synth emulator written in Python that
leverages a [Leap Motion](https://www.leapmotion.com/) device as a controller for pitch, timber and volume.

Make music waving your hands: now you can.

## Installation

You'll need a [Leap Motion](https://www.leapmotion.com/) device and the
[Leap Motion SDK](https://developer-archive.leapmotion.com/documentation/python/index.html)
installed. You'll need in particular the `Leap.py` script to be somewhere in your Python libpath
as well as the `leapd` executable from the SDK.

You'll ealso need the [PYO](https://github.com/belangeo/pyo) DSP module installed:

```bash
pip install pyo
```

Finally, clone and install this repo:

```bash
git clone https://github.com/BlackLight/theremin
cd theremin
[sudo] python setup.py install
```

## Usage

Plug your Leap Motion, start the `leapd` daemon and make sure that your device is detected:

```bash
[sudo] leapd &
```

Start the theremin:

```bash
theremin
```

Move your hands and enjoy the fun!

You can set the pitch of the sound by moving your right hand up and down, while the height of
the left hand will set the volume. Use the `--left-handed` option to invert the order.

## Options

```
usage: theremin [-h] [--list-audio-outputs] [--list-leap-motions]
                [--audio-output AUDIO_OUTPUT] [--audio-backend AUDIO_BACKEND]
                [--channels CHANNELS] [--discrete] [--left-handed]
                [--generator GENERATOR] [--min-frequency MIN_FREQUENCY]
                [--max-frequency MAX_FREQUENCY] [--min-note MIN_NOTE]
                [--max-note MAX_NOTE]

optional arguments:
  -h, --help            show this help message and exit
  --list-audio-outputs, -l
                        List the available audio output devices
  --list-leap-motions, -L
                        List the available Leap Motion devices
  --audio-output AUDIO_OUTPUT, -o AUDIO_OUTPUT
                        Select an output audio device by index (see -l)
  --audio-backend AUDIO_BACKEND, -b AUDIO_BACKEND
                        Select the audio backend (default: portaudio).
                        Supported: {"portaudio", "jack", "coreaudio"}
  --channels CHANNELS, -c CHANNELS
                        Number of audio channels (default: 2)
  --discrete, -d        If set then discrete notes will be generated instead
                        of samples over a continuous frequency space (default:
                        false)
  --left-handed         If set then the pitch control will be on the left hand
                        and the volume control on theright hand. Otherwise,
                        the controls are inverted (default: false)
  --generator GENERATOR, -g GENERATOR
                        Wave generator to be used. See http://ajaxsoundstudio.
                        com/pyodoc/api/classes/generators.html. Default:
                        SineLoop
  --min-frequency MIN_FREQUENCY
                        Minimum audio frequency (default: 55 Hz)
  --max-frequency MAX_FREQUENCY
                        Maximum audio frequency (default: 10 kHz)
  --min-note MIN_NOTE   Minimum MIDI note, as a string (e.g. A4)
  --max-note MAX_NOTE   Maximum MIDI note, as a string (e.g. A4)
```
