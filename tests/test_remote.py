from gitsync.remote import RemoteProviderFactory, RemoteProvider
from gitsync.remote import RemoteFactory, Github, Gitlab
from gitsync.remote import RemoteScheme
from gitsync.httpwrapper import HttpClient
from gitsync.repository import Repository
import pytest


class TestRemoteProviderFactory(object):
    def test_given_github_str_and_remoteproviderfactory_when_create_then_github_provider(self):
        remote_provider = RemoteProviderFactory.create("github")
        assert remote_provider == RemoteProvider.GITHUB

    def test_given_gitlab_str_and_remoteproviderfactory_when_create_then_gitlab_provider(self):
        remote_provider = RemoteProviderFactory.create("gitlab")
        assert remote_provider == RemoteProvider.GITLAB

    def test_given_gitlab_uppercase_str_and_remoteproviderfactory_when_create_then_gitlab_provider(self):
        remote_provider = RemoteProviderFactory.create("GITLAB")
        assert remote_provider == RemoteProvider.GITLAB

    def test_given_other_str_and_remoteproviderfactory_when_create_then_keyerror(self):
        with pytest.raises(KeyError):
            RemoteProviderFactory.create("unknown")


class TestRemoteGithub(object):
    def test_given_remoteprovider_github_when_factory_then_get_github_instance(self):
        remote = self._get_remote()
        assert isinstance(remote, Github)

    def _get_remote(self):
        return RemoteFactory.create(RemoteProvider.GITHUB, "", "https://api.github.com", 443)

    def test_given_remoteprovider_unknown_when_factory_then_notimplementederror(self):
        with pytest.raises(NotImplementedError):
            RemoteFactory.create(None, "", "https://api.github.com", 443)

    def test_given_github_remoteprovider_when_init_then_is_set(self):
        remote = self._get_remote()
        assert isinstance(remote.access_token, str)
        assert isinstance(remote.base_url, str)
        assert isinstance(remote.port, int)
        assert isinstance(remote.session, HttpClient)

    def test_given_github_remoteprovider_when_get_user_repositories_then_result(self):
        remote = self._get_remote()
        user = self._get_user()
        repositories = remote.get_user_repositories(user)
        assert len(repositories) > 0
        for repository in repositories:
            assert isinstance(repository, Repository)
            assert RemoteScheme.GIT.value not in repository.uri

    def _get_user(self):
        return "edijon"


class TestRemoteGitlab(object):
    def test_given_remoteprovider_gitlab_when_factory_then_get_gitlab_instance(self):
        remote = self._get_remote()
        assert isinstance(remote, Gitlab)

    def _get_remote(self):
        return RemoteFactory.create(RemoteProvider.GITLAB, "", "https://gitlab.com", 443)

    def test_given_remoteprovider_unknown_when_factory_then_notimplementederror(self):
        with pytest.raises(NotImplementedError):
            RemoteFactory.create(None,  "", "https://gitlab.com", 443)

    def test_given_gitlab_remoteprovider_when_init_then_is_set(self):
        remote = self._get_remote()
        assert isinstance(remote.access_token, str)
        assert isinstance(remote.base_url, str)
        assert isinstance(remote.port, int)
        assert isinstance(remote.session, HttpClient)

    def test_given_gitlab_remoteprovider_when_get_user_repositories_then_result(self):
        remote = self._get_remote()
        user = self._get_user()
        repositories = remote.get_user_repositories(user)
        assert len(repositories) > 0
        for repository in repositories:
            assert isinstance(repository, Repository)
            assert "git://" not in repository.uri

    def _get_user(self):
        return "edijon"
