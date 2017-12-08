import os


class MediaController(object):

    @staticmethod
    def play_pause():
        os.system("xdotool key XF86AudioPlay")

    @staticmethod
    def next_song():
        os.system("xdotool key XF86AudioNext")

    @staticmethod
    def open_pithos():
        os.system("pithos")

    @staticmethod
    def close_pithos():
        os.system("killall pithos")
