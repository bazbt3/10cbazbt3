# How to use 10cbazbt3.py

## First, Failure:
When interacting with the !0Cv4 server using 10cbazbt3, the server feedback appears to be gibberish.  *It's my fault entirely.*

In a nutshell, I'm currently unable to 'translate' the responses returned from the API into anything I can use **within the application.**  Is it text, is it JSON, is it human-readable?  It is all 3 - of course - but I'm a noob.  It's only a matter of time before it clicks into place though, right?

## Second, the Menu again:
````
10cbazbt3 menu:
  b = Blurb (social post)
  p = Post (blog post)
  m = Mentions
  r = Reply

  exit = Exit

Admin:
  sites =  Sites owned by user
  Login =  Login (deletes current auth token!)
  Logout = Logout (deletes current auth token!)

Choice?
````

Self-explanatory, right?  No, not yet.

## Before blogging for the first time:
Important: Please read through the code comments.  The code is currently tailored specifically to *my* Raspberry Pi's folder structure.  It's also setup to post to only *my* blog - see the 'post' subroutine for the variable to edit - *after* running **'sites'** and examining the API feedback.

Please note there are no helpful messages if 10cbazbt3.py gets things wrong.  I've tested the basics but it's very early days right now.

There is more to follow, but for now please take a look at the **[Technical document](/docs/30-technical.md)** - it is a placeholder for now.
