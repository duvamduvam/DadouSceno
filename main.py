import logging.config
import sys

from dadou_utils.misc import Misc
from dadou_utils.utils.status import Status
from dadou_utils.utils_static import LOGGING_CONFIG_FILE, SHUTDOWN_PIN, STATUS_LED_PIN, BASE_PATH, \
    MAIN_THREAD, MULTI_THREAD, SINGLE_THREAD
from dadourobot.actions.audio_manager import AudioManager
from dadourobot.input.global_receiver import GlobalReceiver

Misc.get_system_type()
#sys.path.append('..')

from dadousceno.files.sceno_json_manager import ScenoJsonManager
from dadousceno.actions.relays_sceno import ScenoRelays
from dadousceno.sceno_config import config


print("sys.path : {}".format(sys.path))

#print(dir(board))
print('Starting Sceno')
print("base {} logs {}".format(config[BASE_PATH], config[LOGGING_CONFIG_FILE]))

logging.config.fileConfig(config[LOGGING_CONFIG_FILE], disable_existing_loggers=False)
shutdown_restart = Status(config[SHUTDOWN_PIN], config[STATUS_LED_PIN])

config[MAIN_THREAD] = True
config[SINGLE_THREAD] = True
config[MULTI_THREAD] = False
global_receiver = GlobalReceiver(config)
json_manager = ScenoJsonManager(config)
audio = AudioManager(config, global_receiver, json_manager)
relays = ScenoRelays(config, global_receiver, json_manager)

while True:

    try:
        msg = global_receiver.get_msg()
        if msg:
            audio.update(msg)
            relays.update(msg)

        relays.process()
        audio.process()
        shutdown_restart.process()

    except Exception as err:
        logging.error('exception {}'.format(err), exc_info=True)
