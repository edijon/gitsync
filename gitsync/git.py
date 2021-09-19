"""Client side module, calling system processes for git commands."""
from abc import ABC, abstractmethod
import os
import subprocess


class Git(ABC):
    """Abstract class, parent of all git implementations.
    Clients should depend of git abstraction, not its implementations.
    """
    @abstractmethod
    def clone(self):
        raise NotImplementedError

    @abstractmethod
    def pull(self):
        raise NotImplementedError


class GitFactory(ABC):
    """GitFactory creates git implementation according to OS."""
    @staticmethod
    def create(url: str, name: str, path: str = "") -> Git:
        if os.name == "posix":
            return GitPosix(url, name, path=path)
        else:
            raise NotImplementedError


class GitPosix(Git):
    def __init__(
            self,
            url: str,
            name: str,
            path: str = os.path.dirname(os.path.realpath(__file__))
            ):
        self.url = url
        self.name = name
        self.path = path
        self.full_path = self.path + "/" + self.name

    def clone(self) -> None:
        if not os.path.isdir(self.full_path):
            subprocess.run(["git", "clone", self.url, self.full_path])
        return None

    def pull(self) -> None:
        os.chdir(self.full_path)
        subprocess.run(["git", "pull"])
        return None
