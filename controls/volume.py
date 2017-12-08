import os
import alsaaudio
from controls.exceptions import ValueOutOfRange


class MediaController(object):

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

    def mute(self):
        self.mixer.setvolume(0)

    def play_pause(self):
        os.system("xdotool key XF86AudioPlay")

    def next_song(self):
        os.system("xdotool key XF86AudioNext")

    def open_pithos(self):
        os.system("pithos")

    def close_pithos(self):
        os.system("killall pithos")
