import logging

from dadou_utils.files.abstract_json_manager import AbstractJsonManager
from dadou_utils.utils_static import JSON_RELAYS
from dadousceno.sceno_config import JSON_AUDIOS


#TODO improve json management

class ScenoJsonManager(AbstractJsonManager):
    logging.info("start json manager")

    audios = None
    audio_seq = None

    def __init__(self, config):

        component = [config[JSON_AUDIOS], config[JSON_RELAYS]]

        super().__init__(config, component)

    """def get_audio_seq(self, key):
        result = self.find(self.audio_seq, 'audios_seq', '$.keys[?key ~ ' + key + ']')
        return self.standard_return(result, False, key)

    def get_relay(self, input_key: str):
        if input_key:
            for key, values in self.json_files[self.config[JSON_RELAYS]].items():
                if input_key in values:
                    return key
        else:
            logging.error("input str None")

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
            logging.error("input str None")"""
