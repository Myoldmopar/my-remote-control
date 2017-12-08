import alsaaudio

from controls.exceptions import ValueOutOfRange


class VolumeController(object):
    def __init__(self):
        self.mixer = alsaaudio.Mixer()
        self._increment = 2

    def get_increment(self):
        return self._increment

    def set_increment(self, new_increment):
        if 1 > new_increment > 20:
            raise ValueOutOfRange("Increment must be between 1 and 20")
        self._increment = new_increment

    def up_increment(self):
        current_volume = self.mixer.getvolume()[0]
        new_volume = current_volume + self._increment
        if new_volume > 100:
            new_volume = 100
        self.mixer.setvolume(new_volume)

    def down_increment(self):
        current_volume = self.mixer.getvolume()[0]
        new_volume = current_volume - self._increment
        if new_volume < 0:
            new_volume = 0
        self.mixer.setvolume(new_volume)

    def max_volume(self):
        self.mixer.setvolume(100)

    def toggle_mute(self):
        if self.mixer.getmute() == 0:
            self.mixer.setmute(1)
        else:
            self.mixer.setmute(0)
