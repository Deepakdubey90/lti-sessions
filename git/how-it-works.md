# How it works

## Traditional versioning systems

Store information as a list of file based changes

![Deltas](https://raw.githubusercontent.com/akhilputhiry/lti-sessions/master/git/images/deltas.png)

## GIT: Snapshots, not differences

Git doesn’t think of or store its data as deltas.  
Instead, Git thinks of its data more like a series of snapshots of a miniature filesystem.

![Snapshots](https://raw.githubusercontent.com/akhilputhiry/lti-sessions/master/git/images/snapshots.png)

## Advantages of git

* Most of the operations happens in the local machine
* More integrity: Everything is checksummed
* Data is not deleted, only added - Even if you try you cannot screw up things

## The three states

* Modified: you have changed the file, but not yet in your local database
* Staged: marked for committing
* Committed: data is safely stored in your local database
