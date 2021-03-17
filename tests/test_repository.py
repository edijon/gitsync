from gitsync.repository import Repository

def get_repository():
    return Repository("name", "uri")

def test_init():
    repository = get_repository()
    assert repository.name == "name"
    assert repository.uri == "uri"