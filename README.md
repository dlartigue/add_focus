# add_focus
Quickly add OmniFocus entries from the Windows Command Line.

## Requires:
+ [OmniFocus](https://www.omnigroup.com/omnifocus) & a [Mail Drop](https://support.omnigroup.com/omnifocus-mail-drop/) Email Address
+ Personal Email Address
    + Set up for a gmail address currently, you can change this by altering the `entry.New_Entry` class. 
    + Since this script currently stores the credentials in plain text, it is highly recommended to set up a single purpose gmail account for this utility.
+ Python 3.5+ (Has not been tested on Python 2, might require some adjustment)

## Use

When called, this script will parse a string of text, format it as an email and
send it to your OmniFocus Mail Drop email. This will add a new entry into you
OmniFocus Inbox.

`C:\> add_focus "Title of your Entry; Note for your Entry"`

The script splits the string at the semicolon. Everything preceding the
semicolon is sent as the title, everything after the semicolon is the note. You
can also send an entry with just a title (no semicolon).

## Set Up

1) Update `config.py` to include your account details.
```
FROM_EMAIL = 'email_you_want_to_use@someplace.biz'
EMAIL_PASS = 'your_email_password'
OMNIFOCUS_EMAIL = 'your_maildrop_email@sync.omnigroup.com'
```

* These next steps cover how to make the script easier to run*

2) Move the project directory to where you keep python scripts
    (e.g. `C:\python\Scrpits\`)

3) Add the project directory to your path. Manually, or using something like [Windows Environment Variables Editor](http://eveditor.com/).

4) Associate `.py` files with python.
+ Launch CMD as Admin
```
    C:\> assoc .py=Python
    C:\> ftype Python="C:\where\you\keep\python.exe" "%1" %*
```
5) Add python.exe to PATHEXT (can be done manually using SET, or with [Windows Environment Variables Editor](http://eveditor.com/))

* If you have any issues getting this to work, this [thread](http://stackoverflow.com/questions/1934675/how-to-execute-python-scripts-in-windows) is a good place to start.

## Todo

+ Add encryption to email credentials?

+ Make this into a proper package, which will simplify script installation.
