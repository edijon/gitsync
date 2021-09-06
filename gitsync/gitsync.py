import argparse
from .remote import RemoteFactory, RemoteProvider
from .repository import Repository
from .git import GitFactory


def main() -> None:
    arguments = get_arguments()
    user = arguments.user
    directory = arguments.directory
    provider = get_remote_provider(arguments.provider)
    token = arguments.token
    api_url = arguments.api_url
    api_port = int(arguments.api_port)

    print("Getting remote...\n")
    remote = RemoteFactory.create(provider, token, api_url, api_port)
    repositories = remote.get_user_repositories(user)
    print("Trying to synchronize repositories...\n")
    for repository in repositories:
        synchronize_repository(repository, directory)
    return None


def get_arguments() -> object:
    parser = argparse.ArgumentParser(description='Synchronize user remote git repositories locally.')
    parser.add_argument("user", type=str, help="remote user namespace")
    parser.add_argument("directory", type=str, help="base directory where syncing repositories")
    parser.add_argument("--provider", help="example: github")
    parser.add_argument("--token", help="remote access token")
    parser.add_argument("--api-url", help="example: https://api.github.com", default="https://api.github.com")
    parser.add_argument("--api-port", help="example: 443", default=443)
    return parser.parse_args()


def get_remote_provider(remote_provider: str) -> RemoteProvider:
    if remote_provider and remote_provider.lower() == "github":
        return RemoteProvider.GITHUB
    elif remote_provider and remote_provider.lower() == "gitlab":
        return RemoteProvider.GITLAB
    else:
        raise NotImplementedError


def synchronize_repository(repository: Repository, directory: str) -> None:
    print("Synchronize repository at URL : %s" % (repository.uri))
    git = GitFactory.create(repository.uri, repository.name, path=directory)
    git.clone()
    git.pull()
    print("")
    return None
