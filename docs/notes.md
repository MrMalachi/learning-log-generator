# Learning Log Generator Notes

## Meaningful Commits
~~**Basic:**
`git commit -m <message>`~~

**Detailed:**
`git commit -m <title>: <description>`

* In case you make an error in a recent commit you can run the following command
  * `--amend` (allows you to modify and add changes to the most recent commit)
    *`git commit --amend`

## Commit Types
* `feat`: Commits which adds a new feature
* `fix`: Commits that fixes a bug
* `refactor`: Refactored code that neither fixes a bug nor adds a feature but rewrites/restructures your code
* `chore`: Changes that do not relate to a fix or feature and don't modify src or test files. Basically miscellaneous 
           commits (for example, updating dependencies or modifying .gitignore file)
* `perf`: Commits are special refactor commits geared towards improving performance
* `ci`: Continuous integration related
* `ops`: Commits that affect operational components like infrastructure, deployment, backup, recovery, etc...
* `build`: Changes that affect the build system build tool, ci pipeline, dependencies, project version, etc...
* `docs`: Commits that affect documentation such as the README.md
* `style`: Changes that do not affect the meaning of the code, likely related to code formatting such as white-space, 
           missing semicolons, etc...
* `revert`: Reverts a previous commit
* `test`: Commits that add missing tests or correct existing tests


