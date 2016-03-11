## Here's the code
### Things to note:
* This application `10cbazbt3.py` is being developed on a Raspberry Pi using **Python 3**.
* My code and dependent files are stored in: `~/home/pi/10cv4/` - the directory is mentioned in each subroutine.
* There's a way to go before this is as 'modular' as I'd like.
* What there is, it works - provided a valid auth token is used.
* What there is, it's a noob's first attempt at proper Python *and* interacting with an API.  Please tread carefully.

## Initial history:
(Most recent on top.)

### 2016-03-10: 4th upload:
* Login now only requires user to copy the token from the JSON response and paste it into an input line,
* Fixed 'sites' menu option.

### 2016-03-09: Third upload:
* **Almost-completed:** login & logout (initially REQUIRES manual edit of authtoken.txt.)

### 2016-03-08: Second upload, with the following features in addition to the preceding:
* Authentication/authorisation IDs/tokens moved out of the application into text files,
* **Started:** login & logout (will initially require manual 'save' of data returned from the API.)

### 2016-03-06: First upload, with the following features:
* Post a Blurb - a social post,
* Post a blog entry,
* Collect the most recent 50 mentions, though it's the 'raw' response at this stage,
* Reply to a specific post - the post number is needed at this stage,
* Check what sites a user 'owns'.
