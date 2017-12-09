import alsaaudio


class VolumeController(object):

    Unmuted = 0
    Muted = 1

    def __init__(self):
        self.mixer = alsaaudio.Mixer()  # let it throw an exception if needed, caller should catch it
        self._increment = 4

    def get_volume(self):
        try:
            current_volume = self.mixer.getvolume()[0]
            return {
                'success': True,
                'volume': current_volume
            }
        except IndexError:
            return {
                'success': False,
                'message': 'Invalid mixer volume retrieval, check permissions and system configuration.'
            }

    def up_increment(self):
        current_volume = self.get_volume()
        if not current_volume['success']:
            return current_volume
        else:
            current_volume = current_volume['volume']
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
        self.set_mute_status(new_mute_status=VolumeController.Unmuted)
        return {'success': 'success', 'new_volume': new_volume}

    def down_increment(self):
        current_volume = self.get_volume()
        if not current_volume['success']:
            return current_volume
        else:
            current_volume = current_volume['volume']
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

    def set_mute_status(self, new_mute_status=-1):
        if new_mute_status == VolumeController.Unmuted:
            current_mute_state = VolumeController.Muted
        elif new_mute_status == VolumeController.Muted:
            current_mute_state = VolumeController.Unmuted
        else:
            try:
                current_mute_state = self.mixer.getmute()[0]
            except IndexError:
                return {
                    'success': False,
                    'message': 'Invalid mixer mute state retrieval, check permissions and system configuration.'
                }
        try:
            if current_mute_state == VolumeController.Unmuted:
                self.mixer.setmute(VolumeController.Muted)
                return {'success': 'success', 'muted': True}
            else:
                self.mixer.setmute(VolumeController.Unmuted)
                return {'success': 'success', 'muted': False}
        except Exception:
            return {
                'success': False,
                'message': 'Could not mute/unmute volume, check permissions and system configuration'
            }
