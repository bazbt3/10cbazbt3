## Here's the code
### Things to note:
* This application `10cbazbt3.py` is being developed on a Raspberry Pi using **Python 3**.
* My code and dependent files are stored in: `~/home/pi/10cv4/` - the directory is mentioned in each subroutine.
* There's a way to go before this is as 'modular' as I'd like.
* What there is, it works - provided a valid auth token is used.
* What there is, it's a noob's first attempt at proper Python *and* interacting with an API.  Please tread carefully.

## Changelog:
(Most recent on top.)

### 2016-03-13: v0.15 (Mid-afternoon):
* Completed and tested login status indicator code.
* Added check for the existence of the status indicator file.
* Started work on a Unix timestamp generator subroutine.
* Changed version numbering scheme: 0.1.5 is identical to the old 0.15.  I hope this will be better-suited to recording the magnitude of the changes brought by updates.

### 2016-03-12: v0.14 (Reasonable hour):
* **Enhanced:** Blog posts: Used `posttext = sys.stdin.read()` to allow multi-line posts to be created when [enter] is pressed - rather than *posting* the content.  The post is committed by pressing [ctrl-d] on a new line.  It does not allow editing of lines already committed to the buffer, but it's a start.
* Tidied server responses - now 'Ok.' for `200` success, or 'Something went wrong. Are you logged in?' for `!= 200`.

### 2016-03-10: v0.13 (Late):
* **Usable:** Login now only requires user to copy the token from the JSON response and paste it into an input line,
* Fixed 'sites' menu option.

### 2016-03-09: v0.12 (SillyO'Clock):
* **Almost-completed:** Login & Logout (initially REQUIRES manual edit of authtoken.txt.)

### 2016-03-08: v0.11 (Second upload, with the following features in addition to the preceding):
* Authentication/authorisation IDs/tokens moved out of the application into text files,
* **Started:** Login & Logout (will initially require manual 'save' of data returned from the API.)

### 2016-03-06: v0.10 (First upload, with the following features):
* Post a Blurb - a social post,
* Post a blog entry,
* Collect the most recent 50 mentions, though it's the 'raw' response at this stage,
* Reply to a specific post - the post number is needed at this stage,
* Check what sites a user 'owns'.
