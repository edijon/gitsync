import sys
from gitsync import gitsync

if __name__ == "__main__":
    try:
        gitsync.main()
    except NotImplementedError:
        sys.argv = [sys.argv[0], "-h"]
        gitsync.main()