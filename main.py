import os
import time
from gpiozero import Button


class MusicButton(Button):
    def __init__(self, pin, file_path):
        super(MusicButton, self).__init__(pin)
        self.file_path = file_path
        self.is_playing = False

    def play(self):
        self.is_playing = True
        os.system('omxplayer ./%s' % self.file_path)

    def stop(self):
        os.system('killall omxplayer')


if __name__ == '__main__':
    button = MusicButton(2)

    while True:
        if button.is_pressed:
            button.play()
        time.sleep(0.1)
