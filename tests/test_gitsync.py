import sys
from gitsync import gitsync
import pytest


def test_given_arguments_for_github_when_main_then_run_successfully():
    sys.argv = [sys.argv[0], "edijon", "/tmp", "--provider=github"]
    gitsync.main()


def test_given_arguments_for_gitlab_when_main_then_run_successfully():
    sys.argv = [
        sys.argv[0],
        "edijon",
        "/tmp",
        "--provider=gitlab",
        "--api-url=https://gitlab.com",
        "--api-port=443"
        ]
    gitsync.main()


def test_given_not_enough_arguments_when_main_then_raise_systemexit():
    sys.argv = [sys.argv[0], "edijon"]
    with pytest.raises(SystemExit):
        gitsync.main()


def test_given_unknown_provider_when_main_then_raise_notimplementederror():
    sys.argv = [sys.argv[0], "edijon", "/tmp", "--provider=unknown"]
    with pytest.raises(NotImplementedError):
        gitsync.main()
