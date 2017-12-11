# import os
import subprocess

# from beastcontroller.settings import BASE_DIR
from controls.structures import SuccessfulReturnTypeBase, FailureReturnTypeBase


# import time


class MediaController(object):
    @staticmethod
    def play_pause():
        return_code = subprocess.call(['xdotool', 'key', 'XF86AudioPlay'])
        if return_code == 0:
            return SuccessfulReturnTypeBase()
        else:
            return FailureReturnTypeBase('Couldn\'t toggle play/pause, xdotool exit code: ' + str(return_code))

    @staticmethod
    def next_song():
        return_code = subprocess.call(['xdotool', 'key', 'XF86AudioNext'])
        if return_code == 0:
            return SuccessfulReturnTypeBase()
        else:
            return FailureReturnTypeBase('Couldn\'t trigger next song, xdotool exit code: ' + str(return_code))

    @staticmethod
    def open_pithos():
        # pithos_script = os.path.join(BASE_DIR, 'scripts', 'spawn_pithos.sh')
        # subprocess.call([pithos_script])
        # time.sleep(1)
        # p = subprocess.Popen(['ps', '-A'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # output, _ = p.communicate()
        # if 'pithos' in output:
        #     return {'success': True}
        # else:
        #     return {'success': False, 'message': "Couldn't open Pithos, check if it is installed and on PATH"}
        return FailureReturnTypeBase('Not implemented, couldn\'t get it to properly fork, etc.')

    @staticmethod
    def close_pithos():
        # return_code = subprocess.call(['killall', 'pithos'])
        # if return_code == 0:
        #     return {'success': True}
        # else:
        #     return {'success': False, 'message': "Couldn't kill Pithos, command exit code: " + str(return_code)}
        return FailureReturnTypeBase('Not implemented, couldn\'t get it to properly fork, etc.')
