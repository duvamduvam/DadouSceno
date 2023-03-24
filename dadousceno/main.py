import logging.config
import sys

from dadou_utils.utils.shutdown_restart import ShutDownRestart

from dadourobot.actions.audios import AudioManager
from dadourobot.input.global_receiver import GlobalReceiver
from dadousceno.files.sceno_json_manager import ScenoJsonManager
from dadousceno.sceno_config import SHUTDOWN_PIN, RESTART_PIN, STATUS_LED_PIN

print(sys.path)
#print(dir(board))
print('Starting Sceno')

shutdown_restart = ShutDownRestart(SHUTDOWN_PIN, RESTART_PIN, STATUS_LED_PIN)

sceno_json_manager = ScenoJsonManager()
audio = AudioManager(sceno_json_manager)

global_receiver = GlobalReceiver()

while True:

    try:
        msg = global_receiver.get_msg()
        if msg:
            audio.update(msg)

        shutdown_restart.process()

    except Exception as err:
        logging.error('exception {}'.format(err), exc_info=True)
