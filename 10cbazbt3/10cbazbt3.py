# 10cbazbt3 - a menu to interact with the 10Centuries.org social network.
# (c) Barrie Turner, 2016-03-04 onwards.
# If you want a version number, you can have 2016-03-09(SillyO'Clock) or 0.12.

# Routines based on the curl examples at https://docs.10centuries.org

# Prerequisites:
# Python 3 (this simply will not work in Python 2; not even the menu!)

# Important:
# Created & tested only on a Raspberry Pi 2 B running Raspbian Linux,
# Created using Python 3 (IDLE).
# All this application's data files are currently stored in '/home/pi/10cv4/' on my machine,
# To make *your* application work please check each subroutine and replace the folder location as necessary!
# THIS APPLICATION DOESN'T YET PARSE (JSON), SO API RESPONSES ARE *ALMOST* HUMAN-READABLE!

# SETUP:

# Load an http library:
import requests
# Load time-related stuff:
from time import strftime

# AUTHENTICATION:

# Define 'my_client_guid' GUID variable - read from /home/pi/10cv4/10cv4guid.txt,
# ***The text file MUST exist and contain one line - ONLY the text of the Client Key,***
# It's obtained from your Admin page's https://admin.10centuries.org/apps/
# And must be added by hand!
myclientguidfile = open("/home/pi/10cv4/10cv4guid.txt", "r")
my_client_guid = myclientguidfile.read()

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

# SUBROUTINES:

# Define the 'Blurb' (social post) subroutine:
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
    # Displays the server's response - *all* of it.
    # Will be made better when I can extract data from the server responses.
    print(response.text)
    print("")
    print("Done - see also serverresponse.txt.")
    print ("")
    
# Define the 'Post' (blog post) subroutine:
def post():
    # Input blog post data:
    posttitle = input("Write a blog post title: ")
    posttext = input("Write a blog post: ")
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
    # Displays the server's response - *all* of it.
    # Will be made better when I can extract data from the server responses.
    print(response.text)
    print("")
    print("Done - see also serverresponse.txt.")
    print ("")

# Define the 'Mentions' subroutine:
def mentions():
    # How many mentions posts to retrieve? ***(Doesn't currently work!)***
    mentionscount = input("How many mentions: ")
    mentionscount = str(mentionscount)
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/content/blurbs/mentions'
    data = {'count': mentionscount}
    response = requests.get(url, headers=headers, data=data)
    # Saves the server's response to 'serverresponse.txt':
    file = open("/home/pi/10cv4/servermentionsresponse.txt", "w")
    file.write(response.text)
    file.close()
    # Displays the server's response - *all* of it. Page after page!
    # Will be made better when I can extract data from the server responses.
    print(response.text)
    print("")
    print("Done - see servermentionsresponse.txt.")
    print ("")

# Define the 'Reply' subroutine:
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
    # Displays the server's response onscreen - *all* of it:
    # Will be made better when I can extract data from the server responses.
    print(response.text)
    print("")
    print("Done - see serverresponse.txt.")
    print ("")

# Admin subroutines start here:

# Define the 'Sites' query subroutine:
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
    print ("")

# Define the 'Login' subroutine:
def login():
    # Input account name:
    my_acctname = input("Username (email): ")
    # Input account password:
    my_acctpass = input("Password: ")
    # The login URL:
    url = 'https://api.10centuries.org/auth/login'
    loginheaders = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'client_guid': my_client_guid, 'acctname': my_acctname, 'acctpass': my_acctpass}
    response = requests.post(url, headers=loginheaders, data=data)
    # Saves the server's response to 'loginresponse.txt':
    file = open("/home/pi/10cv4/loginresponse.txt", "w")
    file.write(response.text)
    file.close()
    # Displays the server's response onscreen - *all* of it:
    # Will be made better when I can extract data from the server responses.
    print(response.text)
    print("")
    print("Done - at this stage manually editing loginresponse.txt to remove all-but the Authentication Token is now NECESSARY!")
    print("")
    print("Please exit.")
    print("")

# Define the 'Logout' subroutine:
def logout():
    # The logout URL:
    url = 'https://api.10centuries.org/auth/logout'
    response = requests.post(url, headers=headertokenonly)
    # Saves the server's response to 'logoutresponse.txt':
    file = open("/home/pi/10cv4/logoutresponse.txt", "w")
    file.write(response.text)
    file.close()
    # Displays the server's response onscreen - *all* of it:
    # Will be made better when I can extract data from the server responses.
    print(response.text)
    print("")
    print("Done - see logoutresponse.txt.")
    print ("")

# MENU:

# The menu has no input validation outside valid options:
print("10cbazbt3 menu:")
print("  b = Blurb (social post)")
print("  p = Post (blog post)")
print("  m = Mentions")
print("  r = Reply")
print("")
print("  exit = Exit")
print("")
print("Admin:")
print("  sites =  Sites owned by user")
print("  Login =  Login (deletes current auth token!)")
print("  Logout = Logout (deletes current auth token!)")
print("")

choice = "Little Bobby Tables"
while (choice != 'exit'):
    choice = input("Choice? ")
    print("The chosen option is:" + choice)
    print("")
    if choice == 'b':
        blurb()
    elif choice == 'p':
        post()
    elif choice == 'm':
        mentions()
    elif choice == 'r':
        reply()
    elif choice == 's':
        sites()
    elif choice == 'Login':
        login()
    elif choice == 'Logout':
        logout()

# The menu exits here:
print("You chose 'exit': Goodbye!")
