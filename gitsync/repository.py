class Repository(object):
    """Git repository data structure."""
    def __init__(self, name: str, uri: str):
        self.name = name
        self.uri = uri
