# 10cbazbt3
A Python 3 application for 10Centuries.org.

## What?
I am in the process of creating an application to interact with the social, blogging and podcasting site [10Centuries.org](http://10centuries.org).

## Why?
Because 10Centuries' creator, Jason Irwin (aka @matigo) has made it relatively easy by publishing [the API docs](https://docs.10centuries.org/) early in the evolution of the site.  Though the documentation is incomplete, nay in some instances still evolving, for anyone with programming and/or bash shell script experience it's fairly straightforward getting stuff working.  Working *correctly* though is another matter entirely...

## How?
### First steps:
1. You'll need a 10Cv4 account.  Though the site is out of its limited beta it's currently running on an invite-only basis.
1. It's easy to create a Developer Client Key for a new application.  Simply head to your personal admin page and [create a new application.](https://admin.10centuries.org/apps/)
1. The Client Key appears near the botton of the screen, and is used in the next step.
1. Getting the application authorised is a matter of [following the instructions and understanding the developer rules.](https://docs.10centuries.org/auth)
1. The `curl` examples provided work as-is provided one uses them in a bash script along with one's own account data, being careful to make the script executable (`chmod +x {your_filename}.sh`.)
1. The data returned from the server contains a unique 'access token' (which must be used instead of username and password.)  It's important to note that this token is usable until one logs out from the application, at which point it must be re-authorised.  The Client Key should remain valid but I'm not about to test this until I've got the bugs out of my baby-steps code!

### Security:
Taking the developer rules seriously I was able to create a bash shell script to take the access token out of the main script and into a seperate file, one read when authorisation is necessary - which it is for pretty much every interaction with the 10Cv4 API.  (Pulling posts from the Global post feed is one notable example of a request for whichauthorisation isn't necessary.)

I mention security here because right now I haven't been able to code any into my Python 3 application.  I'm able to post and reply with it, to post to my blog with it, to get mentions from the server with it, to interrogate the API about my account detals with it; yet I'm unable to seperate the access token from within the code.  This is my inexperience showing; I'm *very* new to Python.

I'd considered posting the code here with the access token completely redacted but first steps, must ask Jason before I do.

As far as I understand it, the authentication method is about to change anyway, from X-Auth to OAuth 2.0.  Whether I'll be able to accommodate that change is, well, a great unknown.  I'm happy to be *here* right now!
