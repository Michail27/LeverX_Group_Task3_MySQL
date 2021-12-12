import json
from abc import ABC, abstractmethod


class AbstractRid(ABC):
    @staticmethod
    @abstractmethod
    def read_json(filename):
        pass


class JsonLoad(AbstractRid):

    @staticmethod
    def read_json(filename: str):
        with open(filename, 'r') as file:
            data = json.loads(file.read())
            return data
