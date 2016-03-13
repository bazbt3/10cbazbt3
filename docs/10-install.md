# Installing 10cbazbt3.py
Incomplete, potentially misleading instructions follow.  This is very much a work in progress.

## Prerequisites:
* **A copy of the [/10cbazbt3/10cbazbt3.py](/10cbazbt3/10cbazbt3.py) file.**  Important: Please read through the code comments.  The code is currently tailored specifically to *my* Raspberry Pi's folder structure.  It's also setup to post to only *my* blog - see the 'post' subroutine for the variable to edit - *after* running 'sites' and examining the API feedback.

* **Python 3.** (This won't work with Python 2 without a rewrite.)

* **A [10Centuries.org](http://10centuries.org) account.**  Though the site is out of its limited beta it's currently running on an invite-only basis.

## First steps:
1. [Read the 10Cv4 requirements and developer rules.](https://docs.10centuries.org/auth)  (Incidentally the `curl` examples provided work as-is provided one uses them in a bash script with one's own account data, being careful to make the script executable (`chmod +x {your_auth_script_filename}.sh`.)
1. Create a Developer Client Key.  *This key must never be shared with any third party.*  Head to your personal admin page and [create a new, ***unique-to-you*** application.](https://admin.10centuries.org/apps/)  The Client Key appears near the bottom of the screen, and is used in the next step.
1. **Important: Create a `10cv4guid.txt`** file in the same directory you intend to store 10cbazbt3.py.  It must contain only one line - *only* the Developer Client Key.  *The Developer Client Key must not be shared along with the code.*
1. Copy my [10cbazbt3.py](/10cbazbt3/10cbazbt3.py) code to your machine.
1. Ensure the file is executable - using Linux it's straightforward: navigate to your chosen directory and `chmod +x 10cbazbt3.py` (assuming no name change.)
1. Edit the code directory locations within each subroutine within the 10cbazbt3.py file - to suit the directory location ***you*** wish to store it at.

## Run 10cbazbt3 for the first time:

Either:

* Navigate to the command line, type `python3 10cbazbt3.py`, or
* Open your favourie Python 3 IDE - I use Python 3 (IDLE) - and open then run the file (runs slower than the command line.)

This menu (or something similar) should appear at this point:

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

1. Type `Login` at the prompt - uppercase and lowercase text - the full word.
1. Type your 10Cv4 username (email address!) when prompted by `Username (email): `
1. Type your 10Cv4 Password when prompted by `Password: `

Carefully check the data returned from the server and displayed onscreen.  It should contains a unique 'token' (used instead of username and password.)  If you see a `200` in the midst of the code it's working nicely.  `400`-series codes indicate a little more work to be done.  Here's a not-pretty example of a successful authentication:

`{ "meta": { "code": 200 }, "data": { "token": "{A Valid Authentication Token}" } }`

At this point 10cbazbt3 will ask you to copy the Authentication Token and paste it into an input line.  When that's done, 10cbazbt3 is usable.

To find out how to start posting, blogging, and read about some current limitations, please read the **[Usage document.](/docs/20-usage.md)**
