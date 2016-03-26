# Technical

### Things to note:
* This application `10cbazbt3.py` is being developed on a Raspberry Pi using **Python 3**.
* My code and dependent files are stored in: `~/home/pi/10cv4/` - the directory is mentioned in each subroutine.
* There's a way to go before this is as 'modular' as I'd like.
* What there is, it works - provided a valid developer auth token is used.
* What there is, it's a noob's first attempt at proper Python *and* interacting with an API.  Please tread carefully.

---

## Obsolete text:

### History/Security:
Taking the developer rules seriously I was able to create a bash shell script to take the access token out of the main script and into a seperate file, one read when authorisation is necessary - which it is for pretty much every interaction with the 10Cv4 API.  (Pulling posts from the Global post feed is one notable example of a request for which authorisation isn't necessary.)

I'm pleased beyond measure that I was able to translate the stuff from bash to Python.

I mention security here because right now I ~~haven't been able to code any into my Python 3 application.~~ have some!  I mean that I've authorised, authenticated, I'm able to post and reply with it, to post to my blog with it, to get mentions from the server with it, to interrogate the API about my account detals with it; ~~**yet I'm unable to seperate the access token from within the code.**~~ yet I've only *just* figured out how to save auth data in external files.  This is my inexperience showing; I'm *very* new to Python.

~~I'd considered posting the code here with the access token completely redacted but first steps, must ask Jason before I do.~~  **The code is [here.](/10cbazbt3)**

As far as I understand it, the authentication method is about to change anyway, from X-Auth to OAuth 2.0.  I've been led to believe I won't need to change anything, so I'm just happy to be here and *evolving*, right now!
