"""Add an abstraction between this application and requests library."""
import enum
from typing import Any
import requests


class HttpStatus(enum.Enum):
    OK = 200
    NOT_FOUND = 404
    ERROR = 500


class HttpResponse(object):
    def __init__(self, response: requests.Response):
        self.response = response

    @property
    def length(self) -> int:
        return len(self.json)

    @property
    def json(self) -> Any:
        try:
            decode = self.response.json()
        except Exception:
            decode = {}
        return decode

    def is_status_ok(self) -> bool:
        if self.response.status_code == HttpStatus.OK.value:
            return True
        else:
            return False


class HttpClient(object):
    def __init__(self, base_url: str, port: int, path: str = ""):
        self.base_url = base_url
        self.port = port
        self.path = path

    @property
    def url(self):
        return self.base_url + ":" + str(self.port) + self.path

    def get(self, endpoint: str = "", params: dict = {}) -> HttpResponse:
        url = self.url + endpoint
        response = requests.get(url, params=params)
        return HttpResponse(response)
