import os
import subprocess

class Git(object):
    @staticmethod
    def controller(url: str, name: str, path: str = "") -> object:
        if os.name == "posix":
            return GitPosix(url, name, path = path)
        else:
            raise NotImplementedError
    
    def clone(self):
        raise NotImplementedError

    def pull(self):
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