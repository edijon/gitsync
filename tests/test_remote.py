from gitsync.remote import Remote, RemoteProvider, Github
from gitsync.httpwrapper import HttpClient
from gitsync.repository import Repository
import pytest


def get_remote():
    return Remote.remote(RemoteProvider.GITHUB, "", "https://api.github.com", 443)


def get_user():
    return "edijon"


def test_remote_init():
    with pytest.raises(NotImplementedError):
        Remote()


def test_remote_factory():
    remote = get_remote()
    assert isinstance(remote, Github)


def test_remote_factory_unknown_provider():
    with pytest.raises(NotImplementedError):
        Remote.remote(None, "", "https://api.github.com", 443)


def test_init():
    remote = get_remote()
    assert isinstance(remote.access_token, str)
    assert isinstance(remote.base_url, str)
    assert isinstance(remote.port, int)
    assert isinstance(remote.session, HttpClient)


def test_get_user_repositories():
    remote = get_remote()
    user = get_user()
    repositories = remote.get_user_repositories(user)
    assert len(repositories) > 0
    for repository in repositories:
        assert isinstance(repository, Repository)
        assert "git://" not in repository.uri
