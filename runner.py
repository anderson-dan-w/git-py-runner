import os
import sys
import argparse
import shutil
import stat

## need to tell Windows where git is *BEFORE IMPORTING*
if sys.platform == "win32":
    git_path = r"C:\Program Files (x86)\Git\bin\git.exe"
    os.environ["GIT_PYTHON_GIT_EXECUTABLE"] = git_path
from git import Repo as gitrepo

HOME = os.getenv("HOME") or os.getenv("HOMEPATH")
SCRATCH_DIR = os.path.join(HOME, "scratch")


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
    if not os.path.exists(repo_dir):
        os.makedirs(repo_dir)
    gitrepo.clone_from(repo_url, repo_dir)


def run_repo(repo_name):
    pull_gitrepo(repo_name)
    sys.path.insert(0, get_repo_dir(repo_name))
    import src.main as repo_main
    repo_main.main()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_name", help="git repo name")
    args = parser.parse_args()
    run_repo(args.repo_name)
