from gitsync.repository import Repository


def test_given_name_and_uri_when_init_repository_then_is_set():
    repository = Repository("name", "uri")
    assert repository.name == "name"
    assert repository.uri == "uri"
