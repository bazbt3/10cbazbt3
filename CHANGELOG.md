# CHANGELOG

### Things to note:
* This application `10cbazbt3.py` is being developed on a Raspberry Pi using **Python 3**.
* My code and dependent files are stored in: `~/home/pi/10cv4/` - the directory is mentioned in each subroutine.
* There's a way to go before this is as 'modular' as I'd like.
* What there is, it works - provided a valid developer auth token is used.
* What there is, it's a noob's first attempt at proper Python *and* interacting with an API.  Please tread carefully.

## The Changelog:
(Most recent on top.)

### 2016-03-25: [v0.2.1 (Slimming)](https://github.com/bazbt3/10cbazbt3/commit/a836354958200ef3a43382e25b479b2f532599d9)
* Improved inline reply - automatically adds poster username (good timing @33MHz!)  Need to add 'cc' usernames later,
* Added inline repost - uses API version, but I've left my own code in there for now (it's called 'bazrepostinline'),
* Added inline star - but I'm not sure if it's going to be useful until I can *display* an account's starred posts,
* Started making the code more modular,
* Cutting down on the early-stage saving of server response text to files,
* Retained saving of user-created post text, prior to a potential 'Drafts' routine (to be used in case posts don't send.)

### 2016-03-24: [v0.2.0 (Pretty colours!)](https://github.com/bazbt3/10cbazbt3/commit/558a3549158642343a50158e280f8b1e1687b758)
* Improved: Mentions display,
* Added: Timeline display,
* Added colour within Mentions & Timeline to enhance clarity and reduce the vertical space used for each post,
* Added: [enter] steps through posts one-at-a-time,
* Added: [r]+[enter] adds inline reply in both Mentions and Timeline display,
* Re-ordered the main menu,
* Version numbers bumped to 0.2.x now timeline-related stuff is working well.  10cbazbt3 is no longer a post-only client!
* (It looks like v0.1.x won't go to 11!)

### 2016-03-21: [v0.1.9 (Oooh!)](https://github.com/bazbt3/10cbazbt3/commit/aaa719a0b1de4f08d2b71b14e9c7bce072b1ae35)
* Mentions subroutine now parses poster user/display name & id, adds post time.

### 2016-03-20: [v0.1.8 (Ruby's teatime)](https://github.com/bazbt3/10cbazbt3/commit/1851376796959ca84399cbeae7abdcfa5c7ad7ac)
* The user can now login using only username and password.  (Auth token in API JSON response is now parsed and saved automatically - no longer requiring user to copy and paste into an input line.)

### 2016-03-19: [v0.1.7 (Post-Earth Hour)](https://github.com/bazbt3/10cbazbt3/commit/57066e4ef85c90fc741431d038047871263135c0)
* Begun to display mentions in a conventional, more-readable format.  (Added a JSON decoder within the Mentions subroutine, but one which currently fails to properly parse the poster's display name.)

### 2016-03-14: [v0.1.6 (Evening)](https://github.com/bazbt3/10cbazbt3/commit/d98988c31e1c903566ca98686d1e45ded75b2b3c)
* Obscured password entry in Login subroutine - actually nothing is echoed onscreen.  (It works nicely in a terminal window but errors in Python 3 IDLE and defaults to visible text entry.)

### 2016-03-13: [v0.1.5 (Mid-afternoon)](https://github.com/bazbt3/10cbazbt3/commit/a6030f40431c4d7609914eb19c2c643d33847ab4):
* Completed and tested logged-in status indicator code.
* Added check for the existence of the status indicator file.
* Started work on a Unix timestamp generator subroutine.

### Changed version numbering scheme:
0.1.5 above is identical to the old 0.15.  I hope this will be better-suited to recording the magnitude of the changes brought by updates.  (The commit link above refers to the code updates at 0.15.)

### 2016-03-12: [v0.14 (Reasonable hour)](https://github.com/bazbt3/10cbazbt3/commit/9e45404ff15c3a6b004a36f684005d96a6738ca4):
* **Enhanced:** Blog posts: Used `posttext = sys.stdin.read()` to allow multi-line posts to be created when [enter] is pressed - rather than *posting* the content.  The post is committed by pressing [ctrl-d] on a new line.  It does not allow editing of lines already committed to the buffer, but it's a start.
* Tidied server responses - now 'Ok.' for `200` success, or 'Something went wrong. Are you logged in?' for `!= 200`.

### 2016-03-10: [v0.13 (Late)](https://github.com/bazbt3/10cbazbt3/commit/045bfc774f6e62b2770ff16da644f7c31340fd9f):
* **Usable:** Login now only requires user to copy the token from the JSON response and paste it into an input line,
* Fixed 'sites' menu option.

### 2016-03-09: [v0.12 (SillyO'Clock)](https://github.com/bazbt3/10cbazbt3/commit/69d8f5e6a63f9c5b3eae3b5fa464641496a445fe):
* **Almost-completed:** Login & Logout (initially REQUIRES manual edit of authtoken.txt.)

### 2016-03-08: [v0.11 (Second upload, with the following features in addition to the preceding)](https://github.com/bazbt3/10cbazbt3/commit/0772796c86bd56a615262c95170342f9416d6604):
* Authentication/authorisation IDs/tokens moved out of the application into text files,
* **Started:** Login & Logout (will initially require manual 'save' of data returned from the API.)

### 2016-03-06: [v0.10 (First upload, with the following features)](https://github.com/bazbt3/10cbazbt3/commit/5a41660ea4415d4bd0bee585ec8e16d3ff8b59c6):
* Post a Blurb - a social post,
* Post a blog entry,
* Collect the most recent 50 mentions, though it's the 'raw' response at this stage,
* Reply to a specific post - the post number is needed at this stage,
* Check what sites a user 'owns'.
