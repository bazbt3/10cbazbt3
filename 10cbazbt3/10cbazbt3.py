# 10cbazbt3 - a menu to interact with the 10Centuries.org social network.
# (c) Barrie Turner, 2016-03-04 onwards.
# Routines based on the curl examples at https://docs.10centuries.org
# 
# Prerequisites:
#   Python 3 (this simply will not work in Python 2; not even the menu!)
#   Created & tested only on a Raspberry Pi 2 B running Raspbian Linux.

# Setup:
# Requests is an http library for humans:
import requests
# Time-related stuff.  This may be better in the post() subroutine!
from time import strftime

# *** The 'Authorization' token should be read from an external file. ***
# *** HAVING IT HARDCODED IS INSECURE, liable to invoke Thor's wrath! ***
# This global variable is at least a first step towards sharing the code.
# It MUST be of the form:
# "headers = {'Authorization': '[YOUR 10C API AUTH TOKEN]', 'Content-Type': 'application/x-www-form-urlencoded'}"
# (But without my enclosing double quotes, without square braces.)
# TOKENS REDACTED BELOW!
headers = {'Authorization': '******************************************************', 'Content-Type': 'application/x-www-form-urlencoded'}
# This header contains only the token - used when only an auth header is required:
headertokenonly = {'Authorization': '******************************************************'}

# Define the Blurb (social post) subroutine:
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
    
# Define the Post (blog post) subroutine:
def post():
    # Input blog post data:
    posttitle = input("Write a blog post title: ")
    posttext = input("Write a blog post: ")
    # Adds a post date & time, currently set as 'now':
    postdatetime = strftime("%Y-%m-%d %H:%M:%S")
    # (I decided to not save blog post text to a file for blog posts.)
    # Uses the global header & creates the data to be passed to the url:
    url = 'https://api.10centuries.org/content'
    # Reference: @bazbt3 channel id = 6, site id = 8.
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

# Define the Mentions subroutine:
def mentions():
    # How many mentions posts to retrieve (doesn't currently work!)
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

# Define the Reply subroutine:
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

# Define the Sites query subroutine:
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

# The menu starts here.  It has no input validation outside valid options:
print("10cbazbt3 menu:")
print("  b = Blurb (social post)")
print("  p = Post (blog post)")
print("  m = Mentions")
print("  r = Reply")
print("")
print("Admin:")
print("  s = Sites by user")
print("")
print("  x = eXit")
print("")

choice = "Little Bobby Tables"
while (choice != 'x'):
    choice = input("Choice? ")
    print("The chosen option is:" + choice)
    print("")
    if choice == 'b':
        blurb()
    elif choice == 'p':
        post()
    elif choice == 'm':
        mentions()
    elif choice == 's':
        sites()
    elif choice == 'r':
        reply()

# The menu exits here:
print("You chose X: Goodbye!")
