### some git notes



# Good habits
One branch per feature or fix, with a descriptive name (add-delete-button, fix-save-bug).
Keep master in a working state, and do experiments on branches.
Run git switch master and git pull before creating new branches so you start from the latest code.
Sometimes it's "Main" instead of "Master"



# create new branch and move to it, copy current things, name of branch
git switch -c my-feature

# add changes, commit changes
git add .
git commit -m "Describe what you changed"

# first time push to git
git push --set-upstream origin todoapp_methods

# push to git
git push

# merge to master
git switch master
git merge my-feature

# delete branch
git branch -d my-feature
