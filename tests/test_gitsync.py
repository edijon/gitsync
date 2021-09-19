import sys
from gitsync import gitsync
import pytest


def test_main_successful_github():
    sys.argv = [sys.argv[0], "edijon", "/tmp", "--provider=github"]
    gitsync.main()


def test_main_successful_gitlab():
    sys.argv = [
        sys.argv[0],
        "edijon",
        "/tmp",
        "--provider=gitlab",
        "--api-url=https://gitlab.com",
        "--api-port=443"
        ]
    gitsync.main()


def test_main_exit():
    sys.argv = [sys.argv[0], "edijon"]
    with pytest.raises(SystemExit):
        gitsync.main()


def test_main_unknown_provider():
    sys.argv = [sys.argv[0], "edijon", "/tmp", "--provider=unknown"]
    with pytest.raises(NotImplementedError):
        gitsync.main()
