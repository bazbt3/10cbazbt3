---
Startup-Bug: Requires presence of valid authtoken.txt file - if deleted after successful login but before logout. See issue #28.
---

# What is '10cbazbt3'?
A Python 3 application to interact with the social, blogging and podcasting site [10Centuries.org](http://10centuries.org).  My work here is starting to cover the basics, moving nicely.

## A couple of recent screenshots:
[![screenshot](/images/10cbazbt3_login_success.PNG)](/images/10cbazbt3_login_success.PNG)

[![screenshot](/images/10cbazbt3_timeline.PNG)](/images/10cbazbt3_timeline.PNG)

## What's needed to make this work?
Python 3 and a [10Centuries.org](http://10centuries.org) account.  (I'm new to Python so don't know how much work would be necessary to convert this to Python 2.x.)

### Repo structure:
If you want to know more, the most important things to look at here are:

* The **[Documentation.](/docs/00-index.md)**  A work in progress,
* The [CHANGELOG,](CHANGELOG.md)
* Inside the [10cbazbt3 code folder](/10cbazbt3/).  The code comments will always be more recent than the documentation,
* This README file.

## Why did I do this?
10Centuries creator, Jason Irwin (aka @matigo), made it relatively easy by publishing [the API docs](https://docs.10centuries.org/) early in the evolution of the site.  Though the documentation is incomplete (the site is still evolving!) for anyone with programming and/or bash shell script experience it's fairly straightforward to get stuff working.  Working *correctly* though is another matter entirely...
