# 10cbazbt3 - a menu to interact with the 10Centuries.org social network.
# (c) Barrie Turner, 2016-03-04 onwards.
# Version number: 2016-03-21(Oooh!) or 0.1.9.

# Routines based on the curl examples at https://docs.10centuries.org

# Prerequisites:
# Python 3 (this simply will not work in Python 2; not even the menu!)

# Important:
# Created & tested only on a Raspberry Pi 2 B running Raspbian Linux,
# Created using Python 3 (IDLE).
# All this application's data files are currently stored in '/home/pi/10cv4/',
# APPLICATION DOESN'T YET PARSE JSON WELL; OUTPUT IS ALMOST HUMAN-READABLE!


# SETUP:

# Load Requests http library:
import requests
# Load JSON *in addition to that built into Requests*:
import json
# Load system-specific library:
import sys
# Load time-related library stuff (there may be duplication here):
from time import strftime
import calendar
from datetime import datetime
# Load password library:
import getpass

# Define a global login status indicator:
global loginstatus


# DEFINE SUBROUTINES:

# Define 'menu' subroutine:
def menu():
    print("10cbazbt3 menu:")
    print("  b = Blurb (social post)")
    print("  p = Post (blog post)")
    print("  m = get Mentions")
    print("  r = Reply")
    print("")
    print("  menu = redisplay Menu")
    print("  exit = Exit")
    print("")
    print("Admin:")
    print("  sites =  Sites owned by user")
    print("  Login =  Login (deletes current auth token!)")
    print("  Logout = Logout (deletes current auth token!)")
    print("")


# DEFINE 10C INTERACTIONS:

# Define the 'blurb' (social post) subroutine:
def blurb():
    # Input some text:
    posttext = input("Write some text: ")
    # Saves the input text to 'posttext.txt':
    file = open("/home/pi/10cv4/posttext.txt", "w")
    file.write(posttext)
    file.close()
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/content'
    data = {'content': posttext}
    response = requests.post(url, headers=headers, data=data)
    # Saves the server's response to 'serverresponse.txt':
    file = open("/home/pi/10cv4/serverresponse.txt", "w")
    file.write(response.text)
    file.close()
    # Displays the server's response:
    responsestatus = response.status_code
    if responsestatus == 200:
        print("Ok.")
    elif responsestatus != 200:
        print("Something went wrong. Are you logged in?")
    print("")


# Define the 'post' (blog post) subroutine:
def post():
    # Input blog post data:
    posttitle = input("Write a blog post title: ")
    print("Write a blog post:")
    print("(Press [ctrl-d] to 'save' when you finish writing.)")
    posttext = sys.stdin.read()
    # Adds a post date & time, currently set as 'now':
    postdatetime = strftime("%Y-%m-%d %H:%M:%S")
    # (I decided to not save blog post text to a file for blog posts.)
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/content'
    # IMPORTANT: @bazbt3's channel id = 6, site id = 8.  SUBSTITUTE WITH *YOUR* CHANNEL_ID!
    data = {'title': posttitle, 'content': posttext, 'channel_id': '6', 'send_blurb': 'Y', 'pubdts': postdatetime}
    response = requests.post(url, headers=headers, data=data)
    # Saves the server's response to 'serverresponse.txt':
    file = open("/home/pi/10cv4/serverresponse.txt", "w")
    file.write(response.text)
    file.close()
    # Displays the server's response:
    responsestatus = response.status_code
    if responsestatus == 200:
        print("Ok.")
    elif responsestatus != 200:
        print("Something went wrong. Are you logged in?")
    print("")


# Define the 'mentions' subroutine:
def mentions():
    # How many mentions posts to retrieve?
    mentionscount = input("How many mentions: ")
    mentionscount = str(mentionscount)
    # Uses the global header & creates the data to be passed to the url:
    # Note: only appending mentionscount to the URL works, i.e. fails passed as data.
    url = 'https://api.10centuries.org/content/blurbs/mentions?count=' + mentionscount
    data = {'count': mentionscount}
    response = requests.get(url, headers=headers, data=data)
    # Saves the server's response to 'serverresponse.txt':
    file = open("/home/pi/10cv4/servermentionsresponse.txt", "w")
    file.write(response.text)
    file.close()
    # Displays the server's response, followed by some useful output.
    # Open the 'servermentionsresponse.txt' file and store contents in json_data:
    json_data = open("/home/pi/10cv4/servermentionsresponse.txt", "r")
    # Main routine to decode the data:
    # Adapted from Python 2.x stuff at http://xmodulo.com/how-to-parse-json-string-in-python.html:
    # Main decode routine within an exception handler:
    # Needs tidying up. but works:
    try:
        decoded = json.load(json_data)
        # Pretty printing of json-formatted string:
        # Retained only whilst developing & debugging:
        print (json.dumps(decoded, sort_keys=True, indent=4))
        print("")
        # Extracting useful data from json-formatted string:
        mentionscount = int(mentionscount)
        print("")
        print("-----------")
        # Loops over the number of posts from mentionscount - saves nothing:
        # will fail if mentionscount > the actual number of mentions:
        for i in reversed(range(mentionscount)):
            # Parses the post id:
            postid = decoded['data'][i]['id']
            posttime = decoded['data'][i]['created_at']
            # Parses the poster's username & id:
            posterusername = decoded['data'][i]['account'][0]['username']
            posteruserid = decoded['data'][i]['account'][0]['id']
            # Prints the post id and poster's username & id:
            print("Post " + str(postid) + ", by " + posterusername + " (id: " + str(posteruserid) + "),"  + " at " + posttime)
            print("-----------")
            # Prints the post text:
            print (decoded['data'][i]['content']['text'])
            print("")
            print("-----------")
    # Exception handler ends here:
    except (ValueError, KeyError, TypeError):
        print ("JSON format error")
    # Reminder of the unformatted file location, for the curious:
    print("")
    print("Done - see servermentionsresponse.txt.")
    print("")


# Define the 'reply' subroutine:
def reply():
    # Input a reply-to post number:
    replytoid = input("Post number to reply to: ")
    # Input some text:
    posttext = input("Write some text: ")
    # Saves the input text to 'posttext.txt':
    file = open("/home/pi/10cv4/posttext.txt", "w")
    file.write(posttext)
    file.close()
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/content'
    data = {'reply_to': replytoid, 'content': posttext}
    response = requests.post(url, headers=headers, data=data)
    # Saves the server's response to 'serverresponse.txt':
    file = open("/home/pi/10cv4/serverresponse.txt", "w")
    file.write(response.text)
    file.close()
    # Displays the server's response:
    responsestatus = response.status_code
    if responsestatus == 200:
        print("Ok.")
    elif responsestatus != 200:
        print("Something went wrong. Are you logged in?")
    print("")


# DEFINE 10C ADMIN SUBROUTINES:

# Define 'authorise' subroutine:
def authorise():
    # Define 'headertokenonly' and 'headers' as global variables, with actual values defined below:
    global headertokenonly
    global headers
    # Define 'headertokenonly' global authentication variable - read from /home/pi/10cv4/authtoken.txt,
    # ***The text file MUST exist and contain one line, ONLY the text of the auth token,***
    # It's returned from the API at the end of the 'Login' subroutine,
    # This header contains only the token - used when only an auth header is required,
    authtokenonlyfile = open("/home/pi/10cv4/authtoken.txt", "r")
    authtokenonly = authtokenonlyfile.read()
    headertokenonly = {'Authorization': authtokenonly}
    # Define 'headers' global variable - uses 'authtokenonly' from above,
    # This header is used throughout the application:
    headers = {'Authorization': authtokenonly, 'Content-Type': 'application/x-www-form-urlencoded'}


# Define the 'login' subroutine:
# Getting and applying the auth token is unnecessarily long,
# Requires less of the file i/o:
def login():
    # Input account name:
    my_acctname = input("10C Username (account email address): ")
    # Input account password:
    my_acctpass = getpass.getpass("10C Password (is not shown onscreen): ")
    # Construct the login URL & data passed to the API:
    url = 'https://api.10centuries.org/auth/login'
    loginheaders = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'client_guid': my_client_guid, 'acctname': my_acctname, 'acctpass': my_acctpass}
    response = requests.post(url, headers=loginheaders, data=data)
    # Saves the server's JSON response to 'loginresponse.txt':
    file = open("/home/pi/10cv4/loginresponse.txt", "w")
    file.write(response.text)
    file.close()
    # Extracts the auth token from the JSON file:
    json_data = open("/home/pi/10cv4/loginresponse.txt", "r")
    decoded = json.load(json_data)
    temptoken = decoded['data']['token']
    # Saves just the auth token to authtoken.txt:
    file = open("/home/pi/10cv4/authtoken.txt", "w")
    file.write(temptoken)
    file.close()
    # Re-authorise now:
    authorise()
    print("")
    print("Re-authorised (but check for a 'connected' indicator!)")
    print("")
    setloginstatus("In")


# Define the 'logout' subroutine:
def logout():
    # The logout URL:
    url = 'https://api.10centuries.org/auth/logout'
    response = requests.post(url, headers=headertokenonly)
    # Saves the server's response to 'logoutresponse.txt':
    file = open("/home/pi/10cv4/logoutresponse.txt", "w")
    file.write(response.text)
    file.close()
    # Indicate that the user is logged out:
    print("You are logged out.")
    print("")
    setloginstatus("Out")


# Define the 'sites' query subroutine:
def sites():
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/users/sites'
    response = requests.get(url, headers=headertokenonly)
    # Saves the server's response to 'serverresponse.txt':
    file = open("/home/pi/10cv4/serverresponse.txt", "w")
    file.write(response.text)
    file.close()
    # Displays the server's response onscreen - *all* of it:
    # Will be made better when I can extract data from the server responses.
    print(response.text)
    print("")
    print("Done - see serverresponse.txt.")
    print("")


# DEFINE MISCELLANEOUS SUBROUTINES:

# Define 'setloginstatus' subroutine:
def setloginstatus(loginstatus):
    file = open("/home/pi/10cv4/loginstatus.txt", "w")
    file.write(loginstatus)
    file.close()


# Define 'checkloginstatusfile' subroutine:
def checkloginstatusfile():
    try:
       open("/home/pi/10cv4/loginstatus.txt")
    except IOError as e:
       print("Please login.")
       setloginstatus("Out")


#Define 'checkloginstatus' subroutine:
def checkloginstatus():
    checkloginstatusfile()
    loginstatusfile = open("/home/pi/10cv4/loginstatus.txt", "r")
    loginstatus = loginstatusfile.read()
    if loginstatus == "Out":
        print("Please login.")
    elif loginstatus == "In":
        print("Connected.")


# Define 'gettime' subroutine:
# DO NOT NOT USE - WORK JUST STARTED!
def gettime():
    d = datetime.utcnow()
    timestamp=calendar.timegm(d.utctimetuple())


# MAIN ROUTINE STARTS:

# AUTHENTICATION:

# Define 'my_client_guid' GUID variable - read from /home/pi/10cv4/10cv4guid.txt,
# ***The text file MUST exist and contain one line - ONLY the text of the Client Key,***
# It's obtained from your Admin page's https://admin.10centuries.org/apps/
# And must be added by hand!
myclientguidfile = open("/home/pi/10cv4/10cv4guid.txt", "r")
my_client_guid = myclientguidfile.read()
# Use the Authentication Token (now handled by 'authorise' subroutine):
authorise()

# MENU STARTS:

# Prints the menu text:
menu()
# The menu has no input validation outside valid options:
choice = "Little Bobby Tables"
while choice != 'exit':
    checkloginstatus()
    choice = input("Choice? ")
    print("")
    if choice == 'b':
        blurb()
    elif choice == 'p':
        post()
    elif choice == 'm':
        mentions()
    elif choice == 'r':
        reply()
    elif choice == 'menu':
        menu()
    elif choice == 'sites':
        sites()
    elif choice == 'Login':
        login()
    elif choice == 'Logout':
        logout()
# The menu exits here once 'exit' is typed:
print("")
print("You chose 'exit': Goodbye!")
