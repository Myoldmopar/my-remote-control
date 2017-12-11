import subprocess

from controls.structures import SuccessfulReturnTypeBase, FailureReturnTypeBase


class MediaController(object):
    """
    This class provides control functions for simulating media keys on the system.
    There is no constructor, as there is no state to persist.
    The functions here require the xdotool command to be available on PATH: apt-get install xdotool
    """

    @staticmethod
    def play_pause():
        """
        This function will attempt to simulate the play/pause media button, either restarting music or pausing it.

        :return: On success, this function returns SuccessfulReturnTypeBase; a FailureReturnTypeBase on failure
        """
        return_code = subprocess.call(['xdotool', 'key', 'XF86AudioPlay'])
        if return_code == 0:
            return SuccessfulReturnTypeBase()
        else:
            return FailureReturnTypeBase('Couldn\'t toggle play/pause, xdotool exit code: ' + str(return_code))

    @staticmethod
    def next_song():
        """
        This function will attempt to simulate the next song media button, which will typically also unpause music.

        :return: On success, this function returns SuccessfulReturnTypeBase; a FailureReturnTypeBase on failure
        """
        return_code = subprocess.call(['xdotool', 'key', 'XF86AudioNext'])
        if return_code == 0:
            return SuccessfulReturnTypeBase()
        else:
            return FailureReturnTypeBase('Couldn\'t trigger next song, xdotool exit code: ' + str(return_code))
