import os
import sys

from dadou_utils.utils.time_utils import TimeUtils
from dadourobot.actions.audio_manager import AudioManager
from dadourobot.tests.conf_test import TestSetup

from dadou_utils.utils_static import AUDIO, KEY, BASE_PATH, AUDIOS_DIRECTORY, STOP
from dadousceno.files.sceno_json_manager import ScenoJsonManager
from dadousceno.sceno_config import config

TestSetup()


import time
import unittest

sys.path.append('../..')

class AudioTests(unittest.TestCase):

    config[BASE_PATH] = "/home/didier/deploy"
    config[AUDIOS_DIRECTORY] = config[BASE_PATH] + '/audios/'

    json_manager = ScenoJsonManager(config)

    audio = AudioManager(config, None, json_manager)

    def test_key_seq(self):
        msg = {KEY: "A9"}
        self.audio.update(msg)
        time.sleep(1000)

    #TODO fix path pb
    def test_audio(self):
        msg = {AUDIO: "song/lacrimosa.mp3"}
        self.audio.update(msg)
        time.sleep(10)
        msg = {AUDIO: STOP}
        self.audio.update(msg)
        starttime = TimeUtils.current_milli_time()
        while not TimeUtils.is_time(starttime, 10000):
            self.audio.process()

    def test_audio_fondu(self):
        msg = {AUDIO: "song/lacrimosa.mp3"}
        self.audio.update(msg)
        time.sleep(10)
        self.audio.stop_sound_fondu()

    """
    @unittest.skip
    def test_playsound(self):
        sound = input(Config.BASE_PATH + "audios/gig.wav")
        playsound(sound)
        time.sleep(10000)


    def test_vlc2(self):
        logging.info("test vlc play : " + Config.BASE_PATH + "audios/gig.wav")
        player = vlc.MediaPlayer(Config.BASE_PATH + "audios/gig.wav")
        player.play()
        while True:
            time.sleep(10)
                """
