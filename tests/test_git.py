from gitsync.git import Git, GitFactory, GitPosix
import pytest
import os


def test_git():
    with pytest.raises(NotImplementedError):
        os.name = "none"
        get_git()
    os.name = "posix"


def get_git():
    return GitFactory.create("https://github.com/edijon/gitsync.git", "gitsync", "/tmp")


def test_posix_init():
    git = get_git()
    assert isinstance(git.url, str)
    assert isinstance(git.name, str)
    assert isinstance(git.path, str)
    assert isinstance(git.full_path, str)
    assert git.full_path == git.path + "/" + git.name


def test_posix_git_factory():
    git = get_git()
    assert isinstance(git, GitPosix)
    assert issubclass(git.__class__, Git)


def test_posix_clone():
    git = get_git()
    git.clone()


def test_posix_pull():
    git = get_git()
    git.pull()
