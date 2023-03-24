import logging
import jsonpath_rw_ext

from dadou_utils.files.abstract_json_manager import AbstractJsonManager

from dadourobot.robot_config import JSON_AUDIOS, BASE_PATH, JSON_DIRECTORY

#TODO improve json management

class ScenoJsonManager(AbstractJsonManager):
    logging.info("start json manager")

    audios = None
    audio_seq = None

    def __init__(self):
        super().__init__(BASE_PATH, JSON_DIRECTORY)
        self.audios = self.open_json(JSON_AUDIOS)

    def get_audio_seq(self, key):
        result = self.find(self.audio_seq, 'audios_seq', '$.keys[?key ~ ' + key + ']')
        return self.standard_return(result, False, key)

    @staticmethod
    def get_attribut(json_object, key):
        if key in json_object:
            return json_object[key]
        else:
            return None

    def get_audio_path_by_name(self, name) -> str:
        result = jsonpath_rw_ext.match('$.audios[?name~' + name + ']', self.audios)
        return self.standard_return(result, True, False)

    def get_audios(self, key: str) -> str:
        if key:
            result = jsonpath_rw_ext.match("$.audios[?(keys[*]~'"+key+"')]", self.audios)
            return self.standard_return(result, True, False)
        else:
            logging.error("input str None")
