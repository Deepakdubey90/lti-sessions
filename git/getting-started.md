# Getting Started

## Creating git repo from scratch

Lets create a simple git repository

```
# create a directory
mkdir my-git-repo

# move to the directory
cd my-git-repo

# create README.md file
echo '# This is my git repo' > README.md

# initialize a git repo or convert the directory to a git repo
git init

# check the condition of my working directory
git status

# save my changes
git add README.md
git commit -m 'created README file'

# add remote server
git remote add <alias> <url>

# push the changes to the remote server
git push origin master
```

## Starting to work on a feature

Lets see how to start working on a change

```
# get the updates
git fetch --all

# make sure master is updated
git reset --hard upstream/master

# create feature branch
git checkout -b feature-1

# work on the changes
# .....

# verify the changes made
git diff

# save the changes locally
git add .
git commit -m 'finished feature-1'

# save the changes in remote server
git push upstream feature-1
```
