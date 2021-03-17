import sys
from gitsync import gitsync
import pytest

def test_main_successful():
    sys.argv = [sys.argv[0], "edijon", "/tmp", "--provider=github"]
    gitsync.main()

def test_main_exit():
    sys.argv = [sys.argv[0], "edijon"]
    with pytest.raises(SystemExit):
        gitsync.main()