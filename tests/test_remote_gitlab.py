from gitsync.remote import RemoteFactory, RemoteProvider, Gitlab
from gitsync.httpwrapper import HttpClient
from gitsync.repository import Repository
import pytest


def test_given_remoteprovider_gitlab_when_factory_then_get_gitlab_instance():
    remote = _get_remote()
    assert isinstance(remote, Gitlab)


def _get_remote():
    return RemoteFactory.create(RemoteProvider.GITLAB, "", "https://gitlab.com", 443)


def test_given_remoteprovider_unknown_when_factory_then_notimplementederror():
    with pytest.raises(NotImplementedError):
        RemoteFactory.create(None,  "", "https://gitlab.com", 443)


def test_given_gitlab_remoteprovider_when_init_then_is_set():
    remote = _get_remote()
    assert isinstance(remote.access_token, str)
    assert isinstance(remote.base_url, str)
    assert isinstance(remote.port, int)
    assert isinstance(remote.session, HttpClient)


def test_given_gitlab_remoteprovider_when_get_user_repositories_then_result():
    remote = _get_remote()
    user = _get_user()
    repositories = remote.get_user_repositories(user)
    assert len(repositories) > 0
    for repository in repositories:
        assert isinstance(repository, Repository)
        assert "git://" not in repository.uri


def _get_user():
    return "edijon"
