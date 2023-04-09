import os

import board
from dadou_utils.utils_static import BASE_PATH, MSG_SIZE, NAME, SERIAL_ID, TYPE, NONE, I2C_ENABLED, DEVICES, \
    STOP_ANIMATION_KEYS, \
    I2C_ENABLED, DEVICES_LIST, JSON_VISUALS, JSON_RELAYS, JSON_MAPPINGS, JSON_LIGHTS_SEQUENCE, \
    JSON_LIGHTS, JSON_FACE_SEQUENCE, JSON_EXPRESSIONS, JSON_COLORS, JSON_AUDIO_SEQUENCE, JSON_AUDIOS, JSON_CONFIG, \
    LOOP_DURATION, LEFT_ARM, REYE, LEYE, MOUTHS, RANDOM_ANIMATION_HIGH, RANDOM_ANIMATION_LOW, RANDOM_ANIMATION, \
    EYE_VISUALS_PATH, MOUTH_VISUALS_PATH, MAIN_LOOP_SLEEP, STOP_KEY, RIGHT_ARM_NB, LEFT_ARM_NB, WHEEL_RIGHT_DIR, \
    WHEEL_LEFT_DIR, WHEEL_RIGHT_PWM, WHEEL_LEFT_PWM, HEAD_PWM_NB, LORA_MISO_PIN, LORA_MOSI_PIN, LORA_SCK_PIN, \
    LORA_RESET_PIN, LORA_CS_PIN, STATUS_LED_PIN, RESTART_PIN, SHUTDOWN_PIN, CMD_RIGHT, CMD_LEFT, CMD_BACKWARD, \
    CMD_FORWARD, DIGITAL_CHANNELS_ENABLED, PWM_CHANNELS_ENABLED, LIGHTS_PIN, LIGHTS_LED_COUNT, LIGHTS_START_LED, \
    LIGHTS_END_LED, JSON_DIRECTORY, SEQUENCES_DIRECTORY, LOGGING_CONFIG_FILE, LOGGING_CONFIG_TEST_FILE, AUDIOS_DIRECTORY

config = {}

config[I2C_ENABLED] = True
config[PWM_CHANNELS_ENABLED] = True
config[DIGITAL_CHANNELS_ENABLED] = False

########## RPI PINS #########

config[SHUTDOWN_PIN] = board.D16
config[RESTART_PIN] = board.D20
config[STATUS_LED_PIN] = board.D12

########## I2C SERVO NUMBER #########

config[HEAD_PWM_NB] = 4
config[WHEEL_LEFT_PWM] = 1
config[WHEEL_RIGHT_PWM] = 2
config[WHEEL_LEFT_DIR] = 0
config[WHEEL_RIGHT_DIR] = 3
config[LEFT_ARM_NB] = 8
config[RIGHT_ARM_NB] = 9

config[STOP_KEY] = "Db"
config[MAIN_LOOP_SLEEP] = 0.001

config[BASE_PATH] = os.getcwd()
config[BASE_PATH] = config[BASE_PATH].replace('/tests', '')
config[LOGGING_CONFIG_TEST_FILE] = config[BASE_PATH]+'/../conf/logging-test.conf'
config[LOGGING_CONFIG_FILE] = config[BASE_PATH]+'/conf/logging.conf'
config[JSON_DIRECTORY] = '/json/'
config[AUDIOS_DIRECTORY] = config[BASE_PATH]+'/audios/'

############### JSON FILES ###############

config[JSON_AUDIOS] = 'audios.json'
config[JSON_AUDIO_SEQUENCE] = 'audio_sequence.json'

