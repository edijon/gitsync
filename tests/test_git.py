from gitsync.git import Git, GitFactory, GitPosix
import pytest
import os


def test_given_unknown_os_when_git_then_raise_error():
    with pytest.raises(NotImplementedError):
        os.name = "none"
        _get_git()
    os.name = "posix"


def _get_git():
    return GitFactory.create("https://github.com/edijon/gitsync.git", "gitsync", "/tmp")


def test_given_os_posix_when_git_instance_then_is_set():
    git = _get_git()
    assert isinstance(git.url, str)
    assert isinstance(git.name, str)
    assert isinstance(git.path, str)
    assert isinstance(git.full_path, str)
    assert git.full_path == git.path + "/" + git.name


def test_given_os_posix_when_git_instance_then_is_gitposix_and_git():
    git = _get_git()
    assert isinstance(git, GitPosix)
    assert issubclass(git.__class__, Git)


def test_given_git_instance_when_clone_then_run_successfully():
    git = _get_git()
    git.clone()


def test_given_git_instance_when_pull_then_run_successfully():
    git = _get_git()
    git.pull()
