import alsaaudio

from controls.structures import SuccessfulReturnTypeBase, FailureReturnTypeBase


class SuccessfulVolumeReturnType(SuccessfulReturnTypeBase):
    """
    A structure for unifying return types from the volume-related functions
    """

    def __init__(self, volume):
        """
        Constructor, which accepts a single parameter, the current, or updated, volume.
        :param volume: The current, or updated, volume, as per the call type
        """
        super(SuccessfulVolumeReturnType, self).__init__()
        self.volume = volume

    def to_dict(self):
        """Utility function to convert this structure into a dictionary"""
        base_dict = super(SuccessfulVolumeReturnType, self).to_dict()
        base_dict['volume'] = self.volume
        return base_dict


class SuccessfulMuteReturnType(SuccessfulReturnTypeBase):
    """
    A structure for unifying return types from the mute-related functions
    """

    def __init__(self, muted):
        """
        Constructor, which accepts a single parameter, the current, or updated, mute state.

        :param muted: A boolean to represent the current, or updated, mute state, as per the call type
        """
        super(SuccessfulMuteReturnType, self).__init__()
        self.muted = muted

    def to_dict(self):
        """Utility function to convert this structure into a dictionary"""
        base_dict = super(SuccessfulMuteReturnType, self).to_dict()
        base_dict['muted'] = self.muted
        return base_dict


class VolumeController(object):
    """
    This class provides query and control functions for managing the master volume level of the system.
    The constructor calls the default ALSA mixer constructor, which will look for the master mixer.
    If the mixer cannot be constructed, an exception in the alsaaudio library is allowed to raise directly.
    """

    Unmuted = 0
    """In alsamixer, the unmuted state is captured by integer zero."""

    Muted = 1
    """In alsamixer, the muted state is captured by integer zero."""

    def __init__(self):  # pragma no cover
        self._mixer = alsaaudio.Mixer()  # let it throw an exception if needed, caller should catch it
        self._increment = 4

    def get_volume(self):  # pragma no cover
        """
        This function retrieves the current volume for the system.

        :return: On success, it returns a SuccessfulVolumeReturnType; on failure it returns a FailureReturnTypeBase.
        """
        try:
            current_volume = self._mixer.getvolume()[0]
            return SuccessfulVolumeReturnType(current_volume)
        except IndexError:
            return FailureReturnTypeBase('Invalid _mixer volume retrieval, check permissions and configuration.')

    def up_increment(self):  # pragma no cover
        """
        This function increments the volume of the system.  If the sound was muted, this will unmute it.

        :return: On success, it returns a SuccessfulVolumeReturnType with the current volume;
                 on failure it returns a FailureReturnTypeBase.
        """
        current_volume = self.get_volume()
        if not current_volume.success:
            return current_volume
        else:
            current_volume = current_volume.volume
        new_volume = current_volume + self._increment
        if new_volume > 100:
            new_volume = 100
        try:
            self._mixer.setvolume(new_volume)
        except Exception:
            return FailureReturnTypeBase('Could not set volume, check permissions and system configuration')
        self.set_mute_status(new_mute_status=VolumeController.Unmuted)  # unmute if we are muted
        return SuccessfulVolumeReturnType(new_volume)

    def down_increment(self):  # pragma no cover
        """
        This function decrements the volume of the system.

        :return: On success, it returns a SuccessfulVolumeReturnType with the current volume;
                 on failure it returns a FailureReturnTypeBase.
        """
        current_volume = self.get_volume()
        if not current_volume.success:
            return current_volume
        else:
            current_volume = current_volume.volume
        new_volume = current_volume - self._increment
        if new_volume < 0:
            new_volume = 0
        try:
            self._mixer.setvolume(new_volume)
        except Exception:
            return FailureReturnTypeBase('Could not set volume, check permissions and system configuration')
        return SuccessfulVolumeReturnType(new_volume)

    def set_mute_status(self, new_mute_status=-1):  # pragma no cover
        """
        This function sets or toggles the mute state of the system.  If no argument is provided, mute state is toggled.

        :param new_mute_status: If this is provided, the mute state is coerced to this updated mute state.
        :return: On success, it returns a SuccessfulMuteReturnType with the updated mute state;
                 on failure it returns a FailureReturnTypeBase.
        """
        if new_mute_status == VolumeController.Unmuted:
            current_mute_state = VolumeController.Muted
        elif new_mute_status == VolumeController.Muted:
            current_mute_state = VolumeController.Unmuted
        else:
            try:
                current_mute_state = self._mixer.getmute()[0]
            except IndexError:
                return FailureReturnTypeBase('Could not get mute state, check permissions and system configuration')
        try:
            if current_mute_state == VolumeController.Unmuted:
                self._mixer.setmute(VolumeController.Muted)
                return SuccessfulMuteReturnType(True)
            else:
                self._mixer.setmute(VolumeController.Unmuted)
                return SuccessfulMuteReturnType(False)
        except Exception:
            return FailureReturnTypeBase('Could not mute/unmute volume, check permissions and system configuration')
