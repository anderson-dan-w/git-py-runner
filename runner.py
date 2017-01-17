import os
import sys
import argparse
import shutil
import stat
from git import Repo as gitrepo

SCRATCH_DIR = os.path.join(os.getenv("HOME"), "scratch")


def get_repo_dir(repo_name):
    return os.path.join(SCRATCH_DIR, repo_name)


def pull_gitrepo(repo_name):
    ## if can't delete something because it's not read/write, just
    ## make it read/write, then delete it
    def del_rw(action, name, exc):
        os.chmod(name, stat.S_IWRITE)
        os.remove(name)

    repo_url = "https://git.enova.com/danderson2/" + repo_name
    repo_dir = get_repo_dir(repo_name)
    if os.path.exists(repo_dir):
        shutil.rmtree(repo_dir, onerror=del_rw)
    gitrepo.clone_from(repo_url, repo_dir)


def run_repo(repo_name, repo_args):
    pull_gitrepo(repo_name)
    sys.path.insert(0, get_repo_dir(repo_name))
    import src.main as repo_main
    repo_main.main(*repo_args)


def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_name", metavar="repo-name",
        help="git repo name")
    ## allow users to pass args for repo.main(), even though we can't
    ## know what those args are yet - just bundle them up and pass along
    args, repo_args = parser.parse_known_args(*args)

    run_repo(args.repo_name, repo_args)

if __name__ == "__main__":
    main(sys.argv[1:])
