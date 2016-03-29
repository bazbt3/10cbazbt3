# CHANGELOG
(Most recent on top.)

### 2016-03-27: [v0.2.5 (Bloatware)](https://github.com/bazbt3/10cbazbt3/commit/03eda3e55b75b338a0d13bcc8157d045eeea4464)
**Bug:**
* Without the `authtoken.txt` file the application fails to open.  This is a quite interesting development - and a bar to anyone attempting to use the code.  [See issue #28.](https://github.com/bazbt3/10cbazbt3/issues/28) and the [preliminary flowchart](https://github.com/bazbt3/10cbazbt3/blob/master/docs/30-technical.md#bug-fixing) in th  'Technical' document - which should help fix this.

Enhancements:
* Added own pinned posts (unlike stars, pins don't toggle),
* Added Interactions - though it has limited appeal without the supporting metadata (e.g. who starred, etc.)

### 2016-03-27: [v0.2.4 ("that's very odd")](https://github.com/bazbt3/10cbazbt3/commit/09e3511b092401e4568a399d4016b4c633c80453)
**Bug:**
* **Reposts are disabled** with a 'disabled' message to the user - though none of the code has changed.  I don't understand why, as the routine worked in v0.2.1.  Annoying: when I use 0.2.1's *once-working version* it too fails now.
* See yesterday's changes for more information.

Temporary bug fixes:
* **Own timeline now works** but it's not ideal - it tops out at 49 posts.  I don't know why it's happening *now.*  

### 2016-03-26: [v0.2.3timelinebug (NOW Buggy)](https://github.com/bazbt3/10cbazbt3/commit/dbd7f26554468a1345237c7c309fa1ec5e1ac0c8)
* **TEMPORARY BUGFIX:** v0.2.3 introduced a failure to display the user timeline.  I've reverted from post count data appended to the URL, to sent as data again.  The failure may be related to the addition of global variables, I don't yet know, the day has run out here.

### 2016-03-26: [v0.2.3 (Buggy)](https://github.com/bazbt3/10cbazbt3/commit/3156bd5035a7725a62fbdbe7e0ec7398b3adb957)
Bug fixes:
* User timeline routine passed post count as data - which worked upto 50 posts - instead of appended to the URL, which now works upto the 200-post API limit.

Enhancements:
* Added own blurb listing, though during testing for a future other-user I'm having trouble with certain account ids causing errors,
* Added post pinning inline with the listings - black only at this stage,
* Started to collect user- and OS-specific data into one place - to *eventually* aid new users and cross-platform capability,
* Added more colour and subtle UI improvements (including the menu),
* Moved starred, pinned and reblurbed indicators to the end of the status line to enhance visibility.

### 2016-03-25: [v0.2.2 (Status symbols)](https://github.com/bazbt3/10cbazbt3/commit/46172710faa7a0628bde98901e9e8cec8c7ec26c)
* Added status symbols for a client user mention; for starred, pinned, reblurbed posts; and added the name of the client used to post,
* Spent time making the mention and timeline routines modular by splitting out the common code into a 'timelinebase' routine, hopefully a usable base for when the timeline isn't restricted to a user-chosen *number* of posts.

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
