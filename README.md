# Automating git-repo runs
---
Trying to ease pain of running Windows task scheduler - the entirety of the batch script should reference the main `runner.py` script, with a single argument, the git-repo name.

This will clone a git-repo from `git.enova.com`, and run `src/main.py` from that repo.

 - Currently only configured to run Python scripts.
   - Requires `src/main.py` to exist, with `main()` function that takes no arguments.
 - Currently configured to only run repo's belonging to me (`@danderson2`), but that wouldn't be too hard to change if anyone wanted that functionality.


Sample batch script:

```
"\path\to\python" "\path\to\here\runner.py" "repo_name"
```