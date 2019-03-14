# Introduction

## History: Creative destruction !!

* Linux kernel development team started using a version control system called Bitkeeper in 2002
* In 2005 they broke up (Linux kernel development community & Bitkeeper company)
* This led to the invention of git by the Linux kernel development community

## Behind the screen: Snapshots, not differences

Normal versioning systems: Store information as a list of file based changes

![Deltas](https://raw.githubusercontent.com/akhilputhiry/lti-sessions/master/git/images/deltas.png)

Git doesn’t think of or store its data as deltas.  
Instead, Git thinks of its data more like a series of snapshots of a miniature filesystem.

![Snapshots](https://raw.githubusercontent.com/akhilputhiry/lti-sessions/master/git/images/snapshots.png)
