from .repository import Repository
from .httpwrapper import HttpClient
from enum import Enum, auto


class RemoteProvider(Enum):
    GITHUB = auto()


class Remote(object):
    @staticmethod
    def remote(remote_type: RemoteProvider, access_token: str, base_url: str, port: int):
        if remote_type == RemoteProvider.GITHUB:
            return Github(access_token, base_url, port)
        else:
            raise NotImplementedError

    def get_user_repositories(self, user: str) -> list:
        raise NotImplementedError


class Github(Remote):
    def __init__(self, access_token: str, base_url: str, port: int):
        self.access_token = access_token
        self.base_url = base_url
        self.port = port
        self.session = HttpClient(self.base_url, self.port)

    def get_user_repositories(self, user: str) -> list:
        path = "/users/" + user + "/repos"
        params = {"access_token": self.access_token}
        result = self.session.get(endpoint=path, params=params)
        repositories = []
        for row in result.json:
            repositories.append(self._get_repository(row))
        return repositories

    def _get_repository(self, row: dict) -> Repository:
        name = row["name"]
        uri = self._normalize_uri(row["git_url"])
        return Repository(name, uri)

    def _normalize_uri(self, uri: str) -> str:
        if "git://" in uri:
            return uri.replace("git://", "https://")
