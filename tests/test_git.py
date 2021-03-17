from gitsync.git import Git, GitPosix


def get_git():
    return Git.controller("https://github.com/edijon/gitsync.git", "gitsync", "/tmp")


def test_init():
    git = get_git()
    assert isinstance(git.url, str)
    assert isinstance(git.name, str)
    assert isinstance(git.path, str)
    assert isinstance(git.full_path, str)
    assert git.full_path == git.path + "/" + git.name


def test_git_factory():
    git = get_git()
    assert isinstance(git, GitPosix)
    assert issubclass(git.__class__, Git)


def test_clone():
    git = get_git()
    git.clone()


def test_pull():
    git = get_git()
    git.pull()
