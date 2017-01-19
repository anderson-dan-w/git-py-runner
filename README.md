# Automating git-repo runs
---
Trying to ease pain of running Windows task scheduler - the entirety of the batch script should reference the main `runner.py` script, with a single positional argument, the git-repo name, optional arguments `--github-url` and `--github-user`, followed by any arguments to pass to that repo's `main()`

This will clone a git-repo from `--github-url`, which defaults to `github.com`, belonging to `--github-user`, which defaults to me (`@anderson-dan-w`) and run `src/main.py` from that repo.

 - Currently only configured to run Python scripts
   - Requires `src/main.py` to exist, with `main()` function
   - Any additional arguments not used by `runner.py` will be passed to `src.main()` as a single list of arguments, `src.main.main(args)` (not `main(*args)`, fwiw)


Sample batch script:

```
"\path\to\python" "\path\to\here\runner.py" "repo_name"
```