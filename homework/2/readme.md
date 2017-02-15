$ git branch test1
$ git branch test2

$ git checkout test1
M	homework/2/readme.md
Switched to branch 'test1'

$ vim test.txt
$ git add test.txt

$ git commit -m "committing test.txt"
[test1 7fc9855] committing test.txt
1 file changed, 1 insertion(+)
create mode 100644 test.txt

$ git checkout test2
M	homework/2/readme.md
Switched to branch 'test2'

$ ls
README.md	_config.yml	exam		homework	quiz

# there's no test.txt cause it hasn't been merged and pulled

$ vim test.txt

$ git checkout test1
error: The following untracked working tree files would be overwritten by checkout:
test.txt
Please move or remove them before you switch branches.
Aborting

$ git add test.txt

$ git commit -m "committing test.txt"
[test2 a7e5735] committing test.txt
1 file changed, 1 insertion(+)
create mode 100644 test.txt

$ git checkout master
M	homework/2/readme.md
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.

$ git merge test1
Updating 29d4569..7fc9855
Fast-forward
test.txt | 1 +
1 file changed, 1 insertion(+)
create mode 100644 test.txt

$ ls
README.md	exam		quiz
_config.yml	homework	test.txt

$ git merge test2
Auto-merging test.txt
CONFLICT (add/add): Merge conflict in test.txt
Automatic merge failed; fix conflicts and then commit the result.

# modified a parallel file and system doesn't know which one to choose

$ git checkout test2
test.txt: needs merge
error: you need to resolve your current index first

$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
(use "git push" to publish your local commits)
You have unmerged paths.
(fix conflicts and run "git commit")
(use "git merge --abort" to abort the merge)

Unmerged paths:
(use "git add <file>..." to mark resolution)

both added:      test.txt

Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git checkout -- <file>..." to discard changes in working directory)

modified:   homework/2/readme.md

no changes added to commit (use "git add" and/or "git commit -a")

# branch is ahead of master and has unmerged paths

$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
(use "git push" to publish your local commits)
You have unmerged paths.
(fix conflicts and run "git commit")
(use "git merge --abort" to abort the merge)

Unmerged paths:
(use "git add <file>..." to mark resolution)

both added:      test.txt

Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git checkout -- <file>..." to discard changes in working directory)

modified:   homework/2/readme.md

no changes added to commit (use "git add" and/or "git commit -a")

$ git add test.txt

$ git commit -m "fixed conflict"
[master a34e45b] fixed conflict
'
$ git checkout test2
M	homework/2/readme.md
Switched to branch 'test2'

$ git branch -d test1
error: The branch 'test1' is not fully merged.
If you are sure you want to delete it, run 'git branch -D test1'.

$ git checkout master
M	homework/2/readme.md
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 3 commits.
(use "git push" to publish your local commits)

$ git branch -d test1
Deleted branch test1 (was 7fc9855).

$ git branch
* master
test2

# the message is different cause test1 was not merged with test2, but it was with master

$ git checkout test2
M	homework/2/readme.md
Switched to branch 'test2'

$ git branch -d test2
error: Cannot delete branch 'test2' checked out at '/Users/kreshel/desktop/ECL2017S'

$ git checkout master
M	homework/2/readme.md
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 3 commits.
(use "git push" to publish your local commits)

$ git branch -d test2
Deleted branch test2 (was a7e5735).

$ git branch
* master
