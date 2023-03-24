import os

import board
from dadou_utils.utils_static import MSG_SIZE,  NAME, SERIAL_ID, TYPE, NONE

I2C_ENABLED = False
PWM_CHANNELS_ENABLED = False
DIGITAL_CHANNELS_ENABLED = False

BASE_PATH = os.getcwd()
if "tests" in BASE_PATH:
    BASE_PATH = BASE_PATH.replace('/tests', '')
    LOGGING_CONFIG_FILE = BASE_PATH+'/../conf/logging-test.conf'
else:
    LOGGING_CONFIG_FILE = BASE_PATH+'/../conf/logging.conf'

############### PATH ###############

#LOGGING_CONFIG_FILE = '/../conf/logging.conf'
#TEST_LOGGING_CONFIG_FILE = '/../../conf/logging-test.conf'
JSON_DIRECTORY = '/../json/'
AUDIOS_DIRECTORY = '../audios/'
SEQUENCES_DIRECTORY = '/../json/sequences/'

########## RPI PINS #########

SHUTDOWN_PIN = board.D16
RESTART_PIN = board.D20
STATUS_LED_PIN = board.D12

############### JSON FILES ###############

JSON_CONFIG = 'sceno_config.json'
JSON_AUDIOS = 'audios.json'
JSON_AUDIO_SEQUENCE = 'audio_sequence.json'
