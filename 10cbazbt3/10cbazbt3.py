# 10cbazbt3 - a menu to interact with the 10Centuries.org social network.
# (c) Barrie Turner, 2016-03-04 onwards.
# Version number: 2016-03-29: v0.2.6 (All are welcome)

# Routines based on the curl examples at https://docs.10centuries.org

# Prerequisites:
# Python 3 (this simply will not work in Python 2; not even the menu!)

# Important:
# Tested only on a Raspberry Pi 2 B running Raspbian Linux,
# Created using Python 3 (IDLE).
# All this application's data files are currently stored in '/home/pi/10cv4/',


# SETUP:

# Load Requests http library:
import requests
# Load JSON *in addition to that built into Requests*:
import json
# Load system-specific library:
import sys
# Load Linux OS library:
import os
# Load time-related library stuff (there may be duplication here):
from time import strftime
import calendar
from datetime import datetime
# Load password library:
import getpass
# Load easy colour terminal text:
from colorama import init
init()
from colorama import Fore, Back, Style


# DEFINE GLOBAL VARIABLES:

# Define and assign user-specific global variables:
global accountid  # Used for the user's account id
accountid = '4'   # @bazbt3's account id = '4' - change this to your own!
global channelid  # User's channel_id - used in 'post' (blog posts) *and only to that one channel*
channelid = '6'   # @bazbt3's channel id = '6' - change this to your own!

# Define other global variables:
global loginstatus    # Stores login status indicator
global responsestatus # Stores API response after POST routine


# DEFINE SUBROUTINES:

# Define 'menu' subroutine:
def menu():
    # Using colour from colorama: https://pypi.python.org/pypi/colorama
    # Formatting e.g.: Fore.COLOUR, Back.COLOUR, Style.DIM with e.g. DIM, RED, CYAN, etc.:
    print(Fore.BLACK + Back.WHITE + "10cbazbt3 menu:" + Style.RESET_ALL)
    print(Fore.YELLOW + Style.DIM + "Main:")
    print("  b = Blurb (social post)   m =     Mentions")
    print("  r = Reply                 t =     Timeline")
    print("  blog = create BLOG post   o =     Own blurbs")
    print("                            pins =  PINS")
    print("Admin:")
    print("  Login =  Login     menu =  redisplay Menu")
    print("  Logout = Logout    sites = user's Sites")
    print("  exit =   Exit")
    print(Style.RESET_ALL)


# DEFINE 10C POST INTERACTIONS:

# LOTS OF DUPLICATION HERE!

# Define the 'blurb' (social post) subroutine:
def blurb():
    # Input some text:
    posttext = input(Fore.YELLOW + Style.DIM + "Write some text: " + Style.RESET_ALL)
    # Saves the input text to 'posttext.txt':
    file = open("/home/pi/10cv4/posttext.txt", "w")
    file.write(posttext)
    file.close()
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/content'
    data = {'content': posttext}
    response = requests.post(url, headers=headers, data=data)
    # Displays the server's response:
    responsestatus = response.status_code
    showapiresponse(responsestatus)


# Define the 'post' (blog post) subroutine:
def post():
    # Input blog post data:
    posttitle = input(Fore.YELLOW + Style.DIM + "Write a blog post title: " + Style.RESET_ALL)
    print(Fore.YELLOW + Style.DIM + "Write a blog post:")
    print("(Press [ctrl-d] to 'save' when you finish writing.)" + Style.RESET_ALL)
    posttext = sys.stdin.read()
    # Adds a post date & time, currently set as 'now':
    postdatetime = strftime("%Y-%m-%d %H:%M:%S")
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/content'
    # IMPORTANT: @bazbt3's channel_id = 6. SUBSTITUTE WITH YOUR CHANNEL_ID in global definitions!
    data = {'title': posttitle, 'content': posttext, 'channel_id': channelid, 'send_blurb': 'Y', 'pubdts': postdatetime}
    response = requests.post(url, headers=headers, data=data)
    # Displays the server's response:
    responsestatus = response.status_code
    showapiresponse(responsestatus)


# Define the 'reply' subroutine:
def reply():
    # INEFFICIENT: NEED TO MERGE MOST OF THE CODE FROM THIS AND THE REPLYINLINE SUBROUTINE:
    # Input a reply-to post number:
    replytoid = input(Fore.YELLOW + Style.DIM + "Post number to reply to: " + Style.RESET_ALL)
    # Input some text:
    posttext = input(Fore.YELLOW + Style.DIM + "Write some text (add usernames!): " + Style.RESET_ALL)
    # Saves the input text to 'posttext.txt':
    file = open("/home/pi/10cv4/posttext.txt", "w")
    file.write(posttext)
    file.close()
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/content'
    data = {'reply_to': replytoid, 'content': posttext}
    response = requests.post(url, headers=headers, data=data)
    # Displays the server's response:
    responsestatus = response.status_code
    showapiresponse(responsestatus)


# Define the 'replyinline' subroutine:
# INEFFICIENT: SEE THE REPLY SUBROUTINE:
def replyinline(postidreply, poster):
    # Use the to-be-replied-to post id:
    replytoid = postidreply
    replytoposter = poster
    # Input some text:
    posttext = input(Fore.YELLOW + Style.DIM + "Write some text: " + Style.RESET_ALL)
    # Add '@', username to posttext:
    posttext = ("@" + replytoposter + " " + posttext)
    # Saves the input text to 'posttext.txt':
    file = open("/home/pi/10cv4/posttext.txt", "w")
    file.write(posttext)
    file.close()
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/content'
    data = {'reply_to': replytoid, 'content': posttext}
    response = requests.post(url, headers=headers, data=data)
    # Displays the server's response:
    responsestatus = response.status_code
    showapiresponse(responsestatus)


# Define the 'repostinline' subroutine:
def repostinline(postidrepost):
    # ROUTINE FAILS REPEATEDLY, SEE THE COMMENTED-OUT CODE BELOW - NO SPACE AFTER THE HASHES:
    # REMOVE THESE 3 PRINT LINES FROM A FIXED ROUTINE:
    print("")
    print(Fore.RED + "ReBlurb needs fixing, sorry!" + Style.RESET_ALL)
    print("")
    # Use the to-be-reposted post id:
    #repostid = postidrepost
    # Uses the global header & creates the data to be passed to the url:
    #url = 'https://api.10centuries.org/content/repost/?post_id=' + repostid
    #data = {'post_id': repostid}
    #response = requests.post(url, headers=headers, data=data)
    # Displays the server's response:
    #responsestatus = response.status_code
    #showapiresponse(responsestatus)


# Define the 'starinline' subroutine:
def starinline(postidstar):
    # Use the to-be-starred post id:
    starid = postidstar
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/content/star/'
    data = {'post_id': starid}
    response = requests.post(url, headers=headers, data=data)
    # Displays the server's response:
    responsestatus = response.status_code
    showapiresponse(responsestatus)


# Define the 'pininline' subroutine:
def pininline(postidpin):
    # Use the to-be-starred post id:
    pinid = postidpin
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/content/pin/'
    # Initial pin = colour ('color') black (hex: #000000), may be good to add the other 5 later:
    data = {'post_id': pinid, 'color': '#000000'}
    response = requests.post(url, headers=headers, data=data)
    # Displays the server's response:
    responsestatus = response.status_code
    showapiresponse(responsestatus)


# Define the 'bazrepostinline' subroutine:
# DEPRECATED IN FAVOUR OF API REPOST - SEE REPOSTINLINE ABOVE:
def bazrepostinline(postidrepost, poster, posttext):
    # Input a repost post number:
    repostid = postidrepost
    # Use the user from the post to be reposted:
    repostuser = poster
    # Use the text from the post to be resposted:
    repostposttext = ("RP @" + repostuser + ": " + posttext)
    # Saves the input text to 'posttext.txt':
    file = open("/home/pi/10cv4/posttext.txt", "w")
    file.write(repostposttext)
    file.close()
    # Uses the global header & creates the data to be passed to the url:
    # 'reply_to' retains the link to the originating post, is intentional:
    url = 'https://api.10centuries.org/content'
    data = {'reply_to': repostid, 'content': repostposttext}
    response = requests.post(url, headers=headers, data=data)
    # Displays the server's response:
    responsestatus = response.status_code
    showapiresponse(responsestatus)


# Define the 'inlineinteractions' subroutine:
# Called during the display of timeline posts:
def inlineinteractions(postid, posterusername, decodedposttext):
    # Accepts all keys. Initial setup: [enter] moves to next post, 'r' replies, 'rp' reposts, '*' stars, 'p' pins:
    inlinecommand = input(Fore.BLUE + Style.DIM + "[enter],r,rp,*,p " + Style.RESET_ALL)
    if inlinecommand == "r":
        postidreply = postid
        poster = posterusername
        replyinline(postidreply, poster)
    if inlinecommand == "rp":
        postidrepost = postid
        repostinline(postidrepost)
    if inlinecommand == "*":
        postidstar = postid
        starinline(postidstar)
    if inlinecommand == "p":
        postidpin = postid
        pininline(postidpin)


# DEFINE 10C GET TIMELINE SUBROUTINES:

# Define the 'timelinebase' subroutine:
def timelinebase(passedresponse, passedpostcount):
    response = passedresponse
    postcount = passedpostcount
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
        # Uncomment the next 2 lines whilst developing & debugging:
        # print (json.dumps(decoded, sort_keys=True, indent=4))
        # print("")
        # Extracting useful data from json-formatted string:
        postcount = int(postcount)
        print(Fore.YELLOW + Style.DIM + "-----------")
        print("[enter]:next post, [r]+[enter]:reply, [rp]+[enter]:repost, [*]+[enter]:star, [p]+[enter]:pin..." + Style.RESET_ALL)
        print("")
        # Loops over the number of posts from postcount - saves nothing:
        # will fail if postcount > the actual number of mentions:
        for i in reversed(range(postcount)):
            # Builds the post metadata:
            # Parses the post id:
            postid = decoded['data'][i]['id']
            # Parses the post creation data & time:
            posttime = decoded['data'][i]['created_at']
            # Parses the poster's username & id:
            posterusername = decoded['data'][i]['account'][0]['username']
            posteruserid = decoded['data'][i]['account'][0]['id']
            # Parses and stores 'is_mention', 'you_starred', 'you_pinned' and 'you_reblurbed':
            ismention = decoded['data'][i]['is_mention']
            youstarred = decoded['data'][i]['you_starred']
            youpinned = decoded['data'][i]['you_pinned']
            youreblurbed = decoded['data'][i]['you_reblurbed']
            clientname = decoded['data'][i]['client']['name']
            # Builds ancillary metadata from above:
            statusstring = " [" + clientname + "]"
            if youstarred != False:
                statusstring = statusstring + " *"
            if youpinned != False:
                statusstring = statusstring + " pin"
            if youreblurbed != False:
                statusstring = statusstring + " rb"
            # Builds the post id, poster's username & id, date & time posted & the above items of metadata:
            # Displays the text header:
            if ismention != False:
                print(Fore.BLACK + Back.CYAN + str(postid) + Fore.GREEN + Back.BLACK + " @" + posterusername + " (id:" + str(posteruserid) + ") " + Fore.CYAN + Style.DIM + posttime + statusstring + Style.RESET_ALL)
            else:
                print(Fore.CYAN + str(postid) + Fore.GREEN + Back.BLACK + " @" + posterusername + " (id:" + str(posteruserid) + ") " + Fore.CYAN + Style.DIM + posttime + statusstring + Style.RESET_ALL)
            # Displays the post text:
            decodedposttext = decoded['data'][i]['content']['text']
            print(decodedposttext)
            # Sends 'postid' to the 'inlineinteraction' subroutine,
            # Where [enter] moves to the next post,
            # Other commands are being added:
            inlineinteractions(postid, posterusername, decodedposttext)
    # Exception handler ends here:
    except (ValueError, KeyError, TypeError):
        print ("JSON format error")
    # Mentions timeline up-to-date:
    print("")
    print(Fore.YELLOW + Style.DIM + "Up-to-date.")
    print("-----------" + Style.RESET_ALL)


# Define the 'mentions' subroutine:
def mentions():
    # How many mentions posts to retrieve?
    postcount = input(Fore.YELLOW + Style.DIM + "How many posts? " + Style.RESET_ALL)
    postcount = str(postcount)
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/content/blurbs/mentions?count=' + postcount
    data = {'count': postcount}
    response = requests.get(url, headers=headers, data=data)
    # Pass the API response to 'timelinebase':
    timelinebase(response, postcount)


# Define the 'hometimeline' subroutine:
def hometimeline():
    # How many home timeline posts to retrieve?
    postcount = input(Fore.YELLOW + Style.DIM + "How many posts? " + Style.RESET_ALL)
    postcount = str(postcount)
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/content/blurbs/home?count=' + postcount
    data = {'count': postcount}
    response = requests.get(url, headers=headers, data=data)
    # Pass the API response to 'timelinebase':
    timelinebase(response, postcount)


# Define the 'ownblurbtimeline' subroutine:
# BUGGY AS-OF v0.2.4 - SEE THE COMMENTED-OUT CODE ON THE 'url' ASSIGNMENT LINE:
def ownblurbtimeline():
    # How many own posts to retrieve?
    postcount = input(Fore.YELLOW + Style.DIM + "How many posts? " + Style.RESET_ALL)
    postcount = str(postcount)
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/users/blurbs/' + accountid #+ '?count=' + postcount
    data = {'count': postcount}
    response = requests.get(url, headers=headers, data=data)
    # Pass the API response to 'timelinebase':
    timelinebase(response, postcount)


# Define the 'ownpinstimeline' subroutine:
def ownpinstimeline():
    # How many own pinned posts to retrieve?
    postcount = input(Fore.YELLOW + Style.DIM + "How many posts? " + Style.RESET_ALL)
    postcount = str(postcount)
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/content/blurbs/pins?count=' + postcount
    data = {'count': postcount}
    response = requests.get(url, headers=headers, data=data)
    # Pass the API response to 'timelinebase':
    timelinebase(response, postcount)


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
    # First check if it exists,
    # If it does not, ask the user to login for the first time:
    try:
        open("/home/pi/10cv4/authtoken.txt")
    except IOError as e:
        os.system('clear')
        print("")
        print(Fore.BLACK + Back.WHITE + "10cbazbt3:")
        print("")
        print(Fore.BLACK + Back.RED + "Please Login for the first time." + Style.RESET_ALL)
        print("")
        login()
        tempinput = input(Fore.YELLOW + "Please press [enter] to continue" + Style.RESET_ALL)
    # Then carry on creating the authorisation headers:
    authtokenonlyfile = open("/home/pi/10cv4/authtoken.txt", "r")
    authtokenonly = authtokenonlyfile.read()
    headertokenonly = {'Authorization': authtokenonly}
    # Define the 'headers' global variable using 'authtokenonly' from above,
    # This header is used throughout the application:
    headers = {'Authorization': authtokenonly, 'Content-Type': 'application/x-www-form-urlencoded'}


# Define the 'login' subroutine:
# Getting and applying the auth token is unnecessarily long,
# Requires less of the file i/o:
def login():
    # Input account name:
    my_acctname = input(Fore.YELLOW + Style.DIM + "10C Username (account email address): " + Fore.WHITE)
    # Input account password:
    my_acctpass = getpass.getpass(Fore.YELLOW + Style.DIM + "10C Password (is not shown onscreen): " + Style.RESET_ALL)
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
    # Let the user know the application is authorised:
    print("")
    print(Fore.BLACK + Back.GREEN + "Authorised" + Style.RESET_ALL + Fore.YELLOW + Style.DIM + " (but check for a 'Connected' indicator!)" + Style.RESET_ALL)
    print("")
    setloginstatus("In")
    authorise()


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
        print(Fore.BLACK + Back.RED + "Please Login." + Style.RESET_ALL)
        setloginstatus("Out")


#Define 'checkloginstatus' subroutine:
def checkloginstatus():
    checkloginstatusfile()
    loginstatusfile = open("/home/pi/10cv4/loginstatus.txt", "r")
    loginstatus = loginstatusfile.read()
    if loginstatus == "Out":
        print(Fore.BLACK + Back.RED + "Please Login." + Style.RESET_ALL)
    elif loginstatus == "In":
        print(Fore.GREEN + "Connected." + Style.RESET_ALL)


# Define the 'showapiresponse' subroutine:
# Displays API response to POST routines:
def showapiresponse(responsestatus):
    if responsestatus == 200:
        print(Fore.YELLOW + Style.DIM + "Ok." + Style.RESET_ALL)
    elif responsestatus != 200:
        print("Something went wrong. Are you logged in?")
    print("")


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
# Use the Authentication Token in the 'authorise' subroutine:
authorise()

# MENU STARTS:

# Prints the menu text:
# Linux/OS X clear screen:
# For Windows use: os.system('cls'):
os.system('clear')
menu()
# The menu has no input validation outside valid options:
choice = "Little Bobby Tables"
while choice != 'exit':
    checkloginstatus()
    choice = input(Fore.YELLOW + Style.DIM + "Choice? " + Style.RESET_ALL)
    print("")
    if choice == 'b':
        blurb()
    elif choice == 'blog':
        post()
    elif choice == 'r':
        reply()
    elif choice == 'm':
        mentions()
    elif choice == 't':
        hometimeline()
    elif choice == 'o':
        ownblurbtimeline()
    elif choice == 'pins':
        ownpinstimeline()
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
print("")
