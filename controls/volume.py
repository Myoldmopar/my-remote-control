import alsaaudio

from controls.structures import SuccessfulReturnTypeBase, FailureReturnTypeBase


class SuccessfulVolumeReturnType(SuccessfulReturnTypeBase):
    def __init__(self, volume):
        super(SuccessfulVolumeReturnType, self).__init__()
        self.volume = volume


class SuccessfulMuteReturnType(SuccessfulReturnTypeBase):
    def __init__(self, muted):
        super(SuccessfulMuteReturnType, self).__init__()
        self.muted = muted


class VolumeController(object):

    Unmuted = 0
    Muted = 1

    def __init__(self):
        self.mixer = alsaaudio.Mixer()  # let it throw an exception if needed, caller should catch it
        self._increment = 4

    def get_volume(self):
        try:
            current_volume = self.mixer.getvolume()[0]
            return SuccessfulVolumeReturnType(current_volume)
        except IndexError:
            return FailureReturnTypeBase('Invalid mixer volume retrieval, check permissions and configuration.')

    def up_increment(self):
        current_volume = self.get_volume()
        if not current_volume.success:
            return current_volume
        else:
            current_volume = current_volume.volume
        new_volume = current_volume + self._increment
        if new_volume > 100:
            new_volume = 100
        try:
            self.mixer.setvolume(new_volume)
        except Exception:
            return FailureReturnTypeBase('Could not set volume, check permissions and system configuration')
        self.set_mute_status(new_mute_status=VolumeController.Unmuted)  # unmute if we are muted
        return SuccessfulVolumeReturnType(new_volume)

    def down_increment(self):
        current_volume = self.get_volume()
        if not current_volume.success:
            return current_volume
        else:
            current_volume = current_volume.volume
        new_volume = current_volume - self._increment
        if new_volume < 0:
            new_volume = 0
        try:
            self.mixer.setvolume(new_volume)
        except Exception:
            return FailureReturnTypeBase('Could not set volume, check permissions and system configuration')
        return SuccessfulVolumeReturnType(new_volume)

    def set_mute_status(self, new_mute_status=-1):
        if new_mute_status == VolumeController.Unmuted:
            current_mute_state = VolumeController.Muted
        elif new_mute_status == VolumeController.Muted:
            current_mute_state = VolumeController.Unmuted
        else:
            try:
                current_mute_state = self.mixer.getmute()[0]
            except IndexError:
                return FailureReturnTypeBase('Could not get mute state, check permissions and system configuration')
        try:
            if current_mute_state == VolumeController.Unmuted:
                self.mixer.setmute(VolumeController.Muted)
                return SuccessfulMuteReturnType(True)
            else:
                self.mixer.setmute(VolumeController.Unmuted)
                return SuccessfulMuteReturnType(False)
        except Exception:
            return FailureReturnTypeBase('Could not mute/unmute volume, check permissions and system configuration')
