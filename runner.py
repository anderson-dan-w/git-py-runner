import os
import sys
import argparse
import shutil
import stat

## need to tell Windows where git is *BEFORE IMPORTING*
if sys.platform == "win32":
    git_base = r"C:\{}\Git\bin\git.exe"
    program_files = ["Program Files", "Program Files (x86)"]
    for location in program_files:
        git_path = git_base.format(location)
        if os.path.exists(git_path):
            os.environ["GIT_PYTHON_GIT_EXECUTABLE"] = git_path
            break
    ## yes, this is for-else, not an incorrect if-else
    else:
        raise FileNotFoundError("can't find git.exe")
## ignore flake8 complaint of 'import not at top of file'
from git import Repo as gitrepo  # noqa: E402

## *nix/Mac have $HOME, Windows has $HOMEPATH
HOME = os.getenv("HOME") or os.getenv("HOMEPATH")
SCRATCH_DIR = os.path.join(HOME, "scratch")


def get_repo_dir(repo_name):
    return os.path.join(SCRATCH_DIR, repo_name)


def pull_gitrepo(repo_name, github_url, github_user):
    ## if can't delete something because it's not read/write, just
    ## make it read/write, then delete it
    def del_rw(action, name, exc):
        os.chmod(name, stat.S_IWRITE)
        os.remove(name)

    ## create a local directory to hold the repo
    repo_dir = get_repo_dir(repo_name)
    if os.path.exists(repo_dir):
        shutil.rmtree(repo_dir, onerror=del_rw)
    if not os.path.exists(repo_dir):
        os.makedirs(repo_dir)

    repo_url = "{}/{}/{}".format(github_url, github_user, repo_name)
    gitrepo.clone_from(repo_url, repo_dir)


def run_repo(repo_name, repo_args):
    sys.path.insert(0, get_repo_dir(repo_name))
    import src.main as repo_main
    repo_main.main(repo_args)


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_name", metavar="repo-name",
        help="git repo name")
    parser.add_argument("--github-url", default="https://github.com",
        help="github URL base to access repo")
    parser.add_argument("--github-user", default="anderson-dan-w",
        help="github user whose repo to check out")
    ## allow users to pass args for repo.main(), even though we can't
    ## know what those args are yet - just bundle them up and pass along
    args, repo_args = parser.parse_known_args(args)

    pull_gitrepo(args.repo_name, args.github_url, args.github_user)
    run_repo(args.repo_name, repo_args)

if __name__ == "__main__":
    main(sys.argv[1:])
