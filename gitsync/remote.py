"""Module for git remotes like Github, Gitlab."""
from .repository import Repository
from .httpwrapper import HttpClient
from enum import Enum, auto
from abc import ABC, abstractmethod


class RemoteProvider(Enum):
    """Define possible remote providers here."""
    GITHUB = auto()
    GITLAB = auto()


class RemoteProviderFactory(object):
    """Create RemoteProvider objects"""
    @staticmethod
    def create(remote_provider: str) -> RemoteProvider:
        remotes = {
            "github": RemoteProvider.GITHUB,
            "gitlab": RemoteProvider.GITLAB}
        return remotes[remote_provider.lower()]


class RemoteScheme(Enum):
    GIT = "git://"
    HTTPS = "https://"


class Remote(ABC):
    """Every remote provider should inherit from this class.
    Clients should depend of remote abstraction not its implementations.
    """
    @abstractmethod
    def get_user_repositories(self, user: str) -> list:
        raise NotImplementedError


class RemoteFactory(ABC):
    """RemoteFactory creates remote implementation according to RemoteType."""
    @staticmethod
    def create(
            remote_type: RemoteProvider,
            access_token: str,
            base_url: str,
            port: int) -> Remote:
        if remote_type == RemoteProvider.GITHUB:
            return Github(access_token, base_url, port)
        elif remote_type == RemoteProvider.GITLAB:
            return Gitlab(access_token, base_url, port)
        else:
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
        if RemoteScheme.GIT.value in uri:
            uri = uri.replace(RemoteScheme.GIT.value, RemoteScheme.HTTPS.value)
        return uri


class Gitlab(Remote):
    def __init__(self, access_token: str, base_url: str, port: int):
        self.access_token = access_token
        self.base_url = base_url
        self.port = port
        self.session = HttpClient(self.base_url, self.port)

    def get_user_repositories(self, user: str) -> list:
        path = "/api/v4/users/" + user + "/projects"
        params = {"PRIVATE-TOKEN": self.access_token}
        result = self.session.get(endpoint=path, params=params)
        repositories = []
        for row in result.json:
            repositories.append(self._get_repository(row))
        return repositories

    def _get_repository(self, row: dict) -> Repository:
        name = row.get("path_with_namespace")
        uri = row.get("http_url_to_repo")
        return Repository(name, uri)
