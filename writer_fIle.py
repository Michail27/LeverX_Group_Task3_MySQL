import json
from abc import ABC, abstractmethod
from xml.dom.minidom import parseString

from dicttoxml import dicttoxml


class AbstractWriter(ABC):
    @staticmethod
    @abstractmethod
    def write(result_list, name):
        pass


class JsonWriter(AbstractWriter):
    @staticmethod
    def write(result_list, name):
        with open('{}.json'.format(name), 'w') as f:
            f.write(json.dumps(result_list, indent=6))


class XmlWriter(AbstractWriter):
    @staticmethod
    def write(result_list, name):
        xml_doc = dicttoxml(result_list, attr_type=False).decode('utf-8')
        pars_xml = parseString(xml_doc)
        with open('{}.xml'.format(name), "w") as f:
            pars_xml.writexml(f, indent='\n', addindent='\t')
