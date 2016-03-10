# Installing 10cbazbt3.py
Incomplete, potentially misleading instructions follow.  This is very much a work in progress.

## Prerequisites:
**A copy of the [/10cbazbt3/10cbazbt3.py](/10cbazbt3/10cbazbt3.py) file.**  Important: Please read through the code comments.  The code is currently tailored specifically to *my* Raspberry Pi's folder structure.

**Python 3.** (This won't work with Python 2 without a rewrite.)

**A [10Centuries.org](http://10centuries.org) account.**  Though the site is out of its limited beta it's currently running on an invite-only basis.

## First steps:
1. Create a Developer Client Key.  *This key must never be shared with any third party.*  Head to your personal admin page and [create a new, ***unique-to-you*** application.](https://admin.10centuries.org/apps/)  The Client Key appears near the botton of the screen, and is used in the next step.
1. **THIS BIT NEEDS WORK - I'M EVEN CONFUSING MYSELF THIS LUNCHTIME!**  Authorise ***your*** unique application.  It is a matter of following the instructions - ***currently only within my code*** - and [understanding the 10Cv4 requirements and developer rules.](https://docs.10centuries.org/auth)  Incidentally the `curl` examples provided work as-is provided one uses them in a bash script with one's own account data, being careful to make the script executable (`chmod +x {your_auth_script_filename}.sh`.
1. Check the data returned from the server, which should contains a unique 'access token' (which must be used instead of username and password.)  If you see 200 codes it's working nicely.  400-series codes indicate a little more work to be done.
1. Copy my [10cbazbt3.py](/10cbazbt3/10cbazbt3.py) code to your machine.
1. Edit the directory locations within each subroutine within the 10cbazbt3.py file - to suit the directory location ***you*** wish to store it at.
1. Make sure the file is executable - using Linux it's straightforward: navigate to your chosen direcdtory and `chmod +x 10cbazbt3.py` (assmunming no name change.)
1. **AT WORK, I'VE FORGOTTEN THE NAME** Create a .txt file - which will store the auth token necessary for the application to run.  Neither this nor the Developer Client Key must be shared with the code.

## To run 10cbazbt3:
Either:

1. Navigate to the command line, type `python3 10cbazbt3.py`, or
1. Open your favourie Python 3 IDE - I use Python 3 (IDLE) - and open then run the file.

## Failure:
In a nutshell, I'm currently unable to 'translate' the responses returned from the API into anything I can use **within the application.**  Is it text, is it JSON, is it human-readable?  It is all 3 - of course - but I'm a noob.  It's only a matter of time before it clicks into place though, right?
