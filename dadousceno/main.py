import logging.config
import sys

from dadou_utils.utils_static import LOGGING_CONFIG_FILE, SHUTDOWN_PIN, RESTART_PIN, STATUS_LED_PIN
from dadou_utils.utils.shutdown_restart import ShutDownRestart

from dadourobot.actions.audios import AudioManager
from dadourobot.input.global_receiver import GlobalReceiver

from dadousceno.files.sceno_json_manager import ScenoJsonManager
from dadousceno.sceno_config import config

#sys.path.append('..')
print("sys.path : {}".format(sys.path))

#print(dir(board))
print('Starting Sceno')

logging.config.fileConfig(config[LOGGING_CONFIG_FILE], disable_existing_loggers=False)

shutdown_restart = ShutDownRestart(config[SHUTDOWN_PIN], config[RESTART_PIN], config[STATUS_LED_PIN])

audio = AudioManager(config, ScenoJsonManager(config))

global_receiver = GlobalReceiver()

while True:

    try:
        msg = global_receiver.get_msg()
        if msg:
            audio.update(msg)

        shutdown_restart.process()

    except Exception as err:
        logging.error('exception {}'.format(err), exc_info=True)
