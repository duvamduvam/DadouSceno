import logging

import adafruit_pcf8574
import board

from dadou_utils.utils.time_utils import TimeUtils
from dadou_utils.utils_static import KEY, I2C_ENABLED, DIGITAL_CHANNELS_ENABLED, RELAY


class ScenoRelays:

    CUT_VOICE = "cut_voice"
    KEY_VOICE = "b"

    def __init__(self, config, receiver, json_manager):

        self.receiver = receiver
        self.config = config
        if not self.config[I2C_ENABLED] or not self.config[DIGITAL_CHANNELS_ENABLED]:
            logging.warning("i2c digital disabled")
            return

        self.json_manager = json_manager

        try:
            i2c = board.I2C()  # uses board.SCL and board.SDA
            pcf = adafruit_pcf8574.PCF8574(i2c, address=0x20)
        except:
            logging.error("i2c 0x20 not reachable")
            self.config[DIGITAL_CHANNELS_ENABLED] = False
            return

        self.voice_out = pcf.get_pin(0)
        self.voice_out.value = False

        self.last_cut_time = 0
        self.cut_timeout = 500

    def update(self, msg):

        if not self.config[I2C_ENABLED] or not self.config[DIGITAL_CHANNELS_ENABLED]:
            return msg

        if msg and KEY in msg and msg[KEY] == self.KEY_VOICE:
            #relay = self.json_manager.get_relay(msg[KEY])
            #if msg[KEY] == self.KEY_VOICE:
            self.voice_out.value = True
            self.last_cut_time = TimeUtils.current_milli_time()
            logging.info("voice off")

        if RELAY in msg and msg[RELAY] == "pitched_voice":
            self.voice_out.value = True
            self.last_cut_time = TimeUtils.current_milli_time()
            logging.info("voice off")

        return msg

    def process(self):

        if not self.config[I2C_ENABLED] or not self.config[DIGITAL_CHANNELS_ENABLED]:
            return

        if self.voice_out.value and TimeUtils.is_time(self.last_cut_time, self.cut_timeout):
            self.voice_out.value = False

            logging.info("voice on")
