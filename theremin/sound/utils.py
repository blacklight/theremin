import math

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
base_c = 24


def midi_to_midi_str(midi):
    """
    :param int midi: MIDI int value (e.g. 69)
    :return: MIDI string (e.g. A4)
    :rtype: str
    """
    global notes, base_c

    assert 24 <= midi <= 127
    i = (midi - base_c) % len(notes)
    octave = int((midi - base_c) / 12) + 1
    return '{note}{octave}'.format(note=notes[i], octave=octave)


def freq_to_midi(freq):
    """
    :param float freq: Frequency (e.g. 440.0)
    :return: MIDI int value (e.g. 69)
    :rtype: int
    """
    return int(math.log2(freq / 440.0) * 12) + 69


def freq_to_midi_str(freq):
    """
    :param float freq: Frequency (e.g. 440.0)
    :return: MIDI string (e.g. A4)
    :rtype: str
    """
    return midi_to_midi_str(freq_to_midi(freq))


def midi_to_freq(midi):
    """
    :param int midi: MIDI note (e.g. 69)
    :return: Frequency in Hz (e.g. 440.0)
    :rtype: float
    """
    return 440.0 * math.pow(2.0, (midi - 69) / 12)


def midi_str_to_midi(midi_str):
    """
    :param str midi_str: MIDI string (e.g. A4)
    :return: MIDI int value (e.g. 69)
    :rtype: int
    """
    global notes, base_c

    note = notes.index(midi_str[0].upper())
    octave = int(midi_str[1])
    assert 1 <= octave <= 9
    return 12 + note + 12*octave
