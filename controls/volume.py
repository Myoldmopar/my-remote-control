import alsaaudio

from controls.exceptions import ValueOutOfRange


class VolumeController(object):
    def __init__(self):
        self.mixer = alsaaudio.Mixer()  # let it throw an exception if needed, caller should catch it
        self._increment = 4

    def get_increment(self):
        return self._increment

    def set_increment(self, new_increment):
        if 1 > new_increment > 25:
            raise ValueOutOfRange("Increment must be between 1 and 20")
        self._increment = new_increment

    def up_increment(self):
        try:
            current_volume = self.mixer.getvolume()[0]
        except IndexError:
            return {
                'success': True,
                'message': 'Invalid mixer volume retrieval, check permissions and system configuration.'
            }
        new_volume = current_volume + self._increment
        if new_volume > 100:
            new_volume = 100
        try:
            self.mixer.setvolume(new_volume)
        except Exception:
            return {
                'success': False,
                'message': 'Could not set volume, check permissions and system configuration'
            }
        return {'success': 'success', 'new_volume': new_volume}

    def down_increment(self):
        try:
            current_volume = self.mixer.getvolume()[0]
        except IndexError:
            return {
                'success': True,
                'message': 'Invalid mixer volume retrieval, check permissions and system configuration.'
            }
        new_volume = current_volume - self._increment
        if new_volume < 0:
            new_volume = 0
        try:
            self.mixer.setvolume(new_volume)
        except Exception:
            return {
                'success': False,
                'message': 'Could not set volume, check permissions and system configuration'
            }
        return {'success': 'success', 'new_volume': new_volume}

    def max_volume(self):
        return self.mixer.setvolume(100)

    def toggle_mute(self):
        try:
            current_mute_state = self.mixer.getmute()[0]
        except IndexError:
            return {
                'success': False,
                'message': 'Invalid mixer mute state retrieval, check permissions and system configuration.'
            }
        try:
            if current_mute_state == 0:
                self.mixer.setmute(1)
                return {'success': 'success', 'muted': True}
            else:
                self.mixer.setmute(0)
                return {'success': 'success', 'muted': False}
        except Exception:
            return {
                'success': False,
                'message': 'Could not mute/unmute volume, check permissions and system configuration'
            }
