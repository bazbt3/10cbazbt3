# How to use 10cbazbt3.py

## The Menu:
````
10cbazbt3 menu:
  b = Blurb (social post)
  p = Post (blog post)
  r = Reply
  m = get Mentions
  t = get home Timeline

  menu = redisplay Menu

Admin:
  sites =  Sites owned by user
  Login =  Login
  Logout = Logout
  exit =   Exit

Connected.
Choice? 
````

Self-explanatory, right?  No, not yet.

## A brief primer:

### `b = Blurb (social post)`:
Easy:

1. Type `b`, press [enter],
1. Read the prompt, write some text, press [enter],
1. The post appears at 10C.

---

### `p = Post (blog post)`:
Not quite as straightforward as a Blurb:

1. Type `p`, press [enter],
1. Read the first prompt, write a blog post title, press [enter],
1. Read the second prompt, write some text, some more text, press [enter] as many times as you like - *entry continues,*
1. **To post your text**, ensure your cursor is on a blank line and press [ctrl-d].

#### Before blogging for the first time:
Important: Please read through the code comments.  The code is currently tailored specifically to *my* Raspberry Pi's folder structure.  It's also setup to post to only *my* blog - see the 'post' subroutine for the variable to edit - *after* running **'sites'** and examining the API feedback.

---

### `r = Reply`:
Needs a post number to reply to:

1. Type `r`, press [enter],
1. Read the prompt,
1. Enter the post number you wish to reply to,
1. Write some text, press [enter].

---

### `m = get Mentions`:
Relatively easy to work with:

1. Type `m`, press [enter]
1. Enter the number of mentions you wish to display, press [enter],
1. Read the screen.

A mention *display* is a list of posts, the oldest at the top.  Each post contains the post ID, poster data, the time posted and the post text.  Now in colour.

Typing [enter] advances to the next post, `r` + [enter] replies to the post above the cursor using a slightly-modified version of the main 'reply' routine.

Here's a typical mention:

````
Choice? m

How many posts: 1
-----------
[enter]: next post, [r]+[enter]: reply...
````

`13240` **`@streakmachine (id:14)`** *`2016-03-24T20:22:17Z`*    
**`@bazbt3 Code away! I'm typing away on a number of different things here myself. :D`**

````
Up-to-date.
-----------
Connected.
Choice?
````

Right now there is no database behind this.

---

### `t = get home Timeline`:
Relatively easy to work with:

1. Type `t`, press [enter]
1. Enter the number of posts you wish to display, press [enter],
1. Read the screen.

A timeline *display* is a list of posts, the oldest at the top.  Each post contains the post ID, poster data, the time posted and the post text.  Now in colour.

Typing [enter] advances to the next post, `r` + [enter] replies to the post above the cursor using a slightly-modified version of the main 'reply' routine.

Here's a typical timeline:

````
Choice? t

How many posts: 2
-----------
[enter]: next post, [r]+[enter]: reply...
````

`13240` **`@streakmachine (id:14)`** *`2016-03-24T20:22:17Z`*
**`@bazbt3 Code away! I'm typing away on a number of different things here myself. :D`**

`13244` **`@jextxadore (id:20)`** *`2016-03-24T20:40:06Z`*
**`Typing up my notes from today's absolutely magnificent tasting.`**    
**`The scores I gave to Château Palmer's 2007 and their Alter Ego 2010 are identical to Robert Parker's. Actually, a lot of my scores are unsettlingly similar to his. Freaky.`**

````
Up-to-date.
-----------
Connected.
Choice?
````

Right now there is no database behind this.

---

### `menu = redisplay Menu`
The menu is displayed once when the application starts, can be invoked when not within a post display routine.

1. Type `menu`: it redisplays the menu.

---

## The Admin menu:

### `sites =  Sites owned by user`:
Occasionally useful:

1. Type `sites`: it returns details of the sites, channels owned by the application's current user.

---

### `Login =  Login`:
Relatively easy:

1. Type `Login`,
1. Enter the account email address,
1. Enter the account password,
1. Read the prompt,
1. Check the application is logged in.

---

### `Logout = Logout`
Easy:

1. Type `Logout`.
1. Check that the application has logged out.

---

### `exit = Exit`:
Easy.

1. Type `exit`, press [enter], the application ends.

---

### Miscellaneous:

Please note there are not many helpful messages if 10cbazbt3.py gets things wrong.  I've tested the basics but it's very early days right now.

There is more to follow, but for now please take a look at the **[Technical document](/docs/30-technical.md)** - it is a placeholder for now.
