import Leap

from .sound.utils import freq_to_midi_str, freq_to_midi, midi_to_freq


def list_leap_motions():
    controller = Leap.Controller()
    has_devices = False

    for device in controller.devices:
        has_devices = True
        print('{}'.format(str(device)))

    if not has_devices:
        print('No Leap Motion devices found')


class LeapMotion(Leap.Listener):
    def __init__(self, dsp, track=0, amplitude=.5, min_frequency=55, max_frequency=10000, left_handed=False):
        super().__init__()
        self.dsp = dsp
        self.track = track
        self.amplitude = amplitude
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency
        self.left_handed = left_handed
        self.controller = Leap.Controller()
        self.controller.add_listener(self)

    def on_init(self, controller):
        print('Leap initialized')

    def on_connect(self, controller):
        print('Leap connected')

    def on_disconnect(self, controller):
        print('Leap disconnected')

    def on_exit(self, controller):
        print('Leap exited')

    @staticmethod
    def _get_hands(frame):
        (left, right) = (None, None)

        if len(frame.hands) > 0:
            if len(frame.hands) == 1:
                left = frame.hands[0] if frame.hands[0].is_left else None
                right = frame.hands[0] if frame.hands[0].is_right else None
            else:
                left = frame.hands[0] if frame.hands[0].is_left else frame.hands[1]
                right = frame.hands[1] if frame.hands[0].is_right else frame.hands[1]

        return left, right

    def on_frame(self, controller):
        frame = controller.frame()
        left, right = self._get_hands(frame)
        if not left and not right:
            if self.dsp.is_playing(self.track):
                self.dsp.stop(self.track)
            return

        y_left = left.palm_position[1] if left else None
        y_right = right.palm_position[1] if right else None
        frequency = None
        amplitude = None

        if self.left_handed:
            if y_left:
                frequency = self.y_to_freq(y_left)
            if y_right:
                amplitude = self.y_to_amplitude(y_right)
        else:
            if y_left:
                amplitude = self.y_to_amplitude(y_left)
            if y_right:
                frequency = self.y_to_freq(y_right)

        if frequency:
            if self.dsp.discrete:
                frequency = midi_to_freq(freq_to_midi(frequency))
            self.dsp.set_frequency(self.track, frequency)

            if not self.dsp.is_playing(self.track):
                self.dsp.play(self.track)

        if amplitude:
            self.dsp.set_volume(self.track, amplitude)
            self.amplitude = amplitude

        print('Left hand height: {:.8f}, Right hand height: {:.8f}, Frequency: {:1f}, MIDI: {}, Amplitude: {:4f}'.
              format(y_left or 0, y_right or 0, frequency or 0, freq_to_midi_str(frequency) if frequency else 0,
                     self.amplitude))

    def y_to_freq(self, y):
        y_min_height = 70
        y_max_height = 500
        min_freq = self.min_frequency
        max_freq = self.max_frequency

        y -= y_min_height
        y_max_height -= y_min_height

        frequency = min_freq + ((max_freq*y) / y_max_height)
        if frequency < min_freq:
            return min_freq
        if frequency > max_freq:
            return max_freq

        return frequency

    @staticmethod
    def y_to_amplitude(y):
        y_min_height = 70
        y_max_height = 500
        min_amplitude = 0
        max_amplitude = 1.5

        y -= y_min_height
        y_max_height -= y_min_height
        max_amplitude -= min_amplitude

        amplitude = min_amplitude + ((max_amplitude*y) / y_max_height)
        if amplitude < min_amplitude:
            return min_amplitude
        if amplitude > max_amplitude:
            return max_amplitude

        return amplitude

    def stop(self):
        self.controller.remove_listener(self)
