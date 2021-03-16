from enum import Enum, auto


class Repository(object):
    def __init__(self, name: str, uri: str):
        self.name = name
        self.uri = uri
        