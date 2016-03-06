*Document is a little verbose.*

## What is '10cbazbt3'?
A Python 3 application to interact with the social, blogging and podcasting site [10Centuries.org](http://10centuries.org), aka 10Cv4 - the 4th iteration of the platform.  My work doesn't even properly cover the basics, but it's moving nicely.

## Why did I do this?
10Centuries creator, Jason Irwin (aka @matigo), made it relatively easy by publishing [the API docs](https://docs.10centuries.org/) early in the evolution of the site.  Though the documentation is incomplete (the site is still evolving!) for anyone with programming and/or bash shell script experience it's fairly straightforward to get stuff working.  Working *correctly* though is another matter entirely...

## What's needed to make this work?

### Repo structure:
Firstly, the most important things to look at here are:

* This README file,
* The [Documentation](/docs/README.md) - a work about-to-be in progress.
* Indside the [10cbazbt3 code folder.](/10cbazbt3/)

### You'll need:
1. Python 3 - this won't work with Python 2.
1. A 10Cv4 account.  Though the site is out of its limited beta it's currently running on an invite-only basis.
1. To create a Developer Client Key, simply head to your personal admin page and [create a new application.](https://admin.10centuries.org/apps/)  The Client Key appears near the botton of the screen, and is used in the next step.
1. To authorise your application, it is a matter of [following the instructions and understanding the developer rules.](https://docs.10centuries.org/auth)  The `curl` examples provided work as-is provided one uses them in a bash script along with one's own account data, being careful to make the script executable (`chmod +x {your_filename}.sh`.)
1. The data returned from the server, which contains a unique 'access token' (which must be used instead of username and password.)  It's important to note that this token is usable until one logs out from the application, at which point it must be re-authorised.  The Client Key should remain valid but I'm not about to test this until I've got the bugs out of my baby-steps code!

### Security:
Taking the developer rules seriously I was able to create a bash shell script to take the access token out of the main script and into a seperate file, one read when authorisation is necessary - which it is for pretty much every interaction with the 10Cv4 API.  (Pulling posts from the Global post feed is one notable example of a request for which authorisation isn't necessary.)

I mention security here because right now I haven't been able to code any into my Python 3 application.  I mean that I've authorised, authenticated, I'm able to post and reply with it, to post to my blog with it, to get mentions from the server with it, to interrogate the API about my account detals with it; **yet I'm unable to seperate the access token from within the code.**  This is my inexperience showing; I'm *very* new to Python.

~~I'd considered posting the code here with the access token completely redacted but first steps, must ask Jason before I do.~~  The code is [here.](/10cbazbt3)

As far as I understand it, the authentication method is about to change anyway, from X-Auth to OAuth 2.0.  I've been led to believe I won't need to change anything, so I'm just happy to be here and *evolving*, right now!

## Failure:
In a nutshell, I'm so-far unable to 'translate' the responses returned from the API into anything I can use **within the application.**  Is it text, is it JSON, is it human-readable?  It is all 3 - of course - but I'm a noob.  It's only a matter of time before it clicks into place though, right?
