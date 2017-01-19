# Automating git-repo runs
---
Trying to ease pain of running Windows task scheduler - the entirety of the batch script should reference the main `runner.py` script, with a single argument, the git-repo name, followed by any arguments to pass to that repo's `main()`

This will clone a git-repo from `git.enova.com`, and run `src/main.py` from that repo.

 - Currently only configured to run Python scripts.
   - Requires `src/main.py` to exist, with `main()` function.
   - Any additional arguments not used by `runner.py` will be passed to `src.main()`
 - Currently configured to only run repo's belonging to me (`@danderson2`), but that wouldn't be too hard to change if anyone wanted that functionality.


Sample batch script:

```
"\path\to\python" "\path\to\here\runner.py" "repo_name"
```