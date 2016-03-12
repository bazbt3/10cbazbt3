# How to use 10cbazbt3.py

## The Menu:
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

## A brief primer:

### `b = Blurb (social post)`:
Easy:

1. Type `b`, press [enter],
1. Read the prompt, write some text, press [enter],
1. the post appears at 10C.

### `p = Post (blog post)`:
Not quite as straightforward as a Blurb:

1. Type `p`, press [enter],
1. Read the first prompt, write a blog post title, press [enter],
1. Read the second prompt, write some text, some more text, press [enter] as many times as you like - *entry continues,*
1. **To post your text**, ensure your cursor is on a blank line and press [ctrl-d].

#### Before blogging for the first time:
Important: Please read through the code comments.  The code is currently tailored specifically to *my* Raspberry Pi's folder structure.  It's also setup to post to only *my* blog - see the 'post' subroutine for the variable to edit - *after* running **'sites'** and examining the API feedback.

### `m = Mentions`:
Hard to work with:

1. Type `m`, press [enter]
1. Read the screen.

#### Failure:
When interacting with the !0Cv4 server using 10cbazbt3, the server feedback appears to be gibberish.  Lots of it.  *It's my fault entirely.*

In a nutshell, I'm currently unable to 'translate' the responses returned from the API into anything I can use **within the application.**  Is it text, is it JSON, is it human-readable?  It is all 3 - of course - but I'm a noob.  It's only a matter of time before it clicks into place though, right?

### `r = Reply`:
Reply comes after 'mentions' here for 2 reasons:

* Mentions is *very* incomplete.  It returns the API server response, but extracts nothing meaningful from it.
* The 10C Blurbs screen currently has an anchor with each post - hovering over it gives a post number.  Use that. until this application works!

1. Type `r`, press [enter],
1. Read the prompt,
1. Enter the post number you wish to reply to,
1. Write some text, presse [enter].

### `exit = Exit`:
Easy.

* Type `exit`, press [enter], the application ends.

## The Admin menu:

### `sites =  Sites owned by user`:
Occasionally useful:

1. Type `Logout`: it returns details of the sites, channels owned by the application's current user.

### `Login =  Login (deletes current auth token!)`:
Needs concentration:

1. Type `Login`,
1. Enter the account email address,
1. Enter the account password,
1. Read the prompt,
1. Copy the code *as-indicated* by the prompt,
1. Reposition the cursor on the input line, paste the clipboard contents, press [enter],
1. Check the applicatio is logged in again.

### `Logout = Logout (deletes current auth token!)`
Easy:

1. Type `Logout`.
1. Check that the application has logged out.

---

### Miscellaneous:

Please note there are not many helpful messages if 10cbazbt3.py gets things wrong.  I've tested the basics but it's very early days right now.

There is more to follow, but for now please take a look at the **[Technical document](/docs/30-technical.md)** - it is a placeholder for now.
