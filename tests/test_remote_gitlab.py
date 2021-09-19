from gitsync.remote import RemoteFactory, RemoteProvider, Gitlab
from gitsync.httpwrapper import HttpClient
from gitsync.repository import Repository
import pytest


def test_remote_factory():
    remote = get_remote()
    assert isinstance(remote, Gitlab)


def get_remote():
    return RemoteFactory.create(RemoteProvider.GITLAB, "", "https://gitlab.com", 443)


def test_remote_factory_unknown_provider():
    with pytest.raises(NotImplementedError):
        RemoteFactory.create(None,  "", "https://gitlab.com", 443)


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


def get_user():
    return "edijon"
