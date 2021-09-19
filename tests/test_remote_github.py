from gitsync.remote import RemoteFactory, RemoteProvider, RemoteScheme, Github
from gitsync.httpwrapper import HttpClient
from gitsync.repository import Repository
import pytest


def test_remote_factory():
    remote = get_remote()
    assert isinstance(remote, Github)


def get_remote():
    return RemoteFactory.create(RemoteProvider.GITHUB, "", "https://api.github.com", 443)


def test_remote_factory_unknown_provider():
    with pytest.raises(NotImplementedError):
        RemoteFactory.create(None, "", "https://api.github.com", 443)


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
        assert RemoteScheme.GIT.value not in repository.uri


def get_user():
    return "edijon"
