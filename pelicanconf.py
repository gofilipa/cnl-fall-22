AUTHOR = 'Filipa Calado'
SITENAME = 'Coding Natural Language Fall 2022'
SITEURL = 'https://gofilipa.github.io/cnl-fall-22'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

## FC EDITs: 


## Customizing the navbar

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Syllabus', '/pages/syllabus.html'),
    ('Course Schedule', 'cnl-fall-22/pages/course_schedule.html'),
    ('Homework', '/pages/homework.html'),
    ('Submit Homework', 'https://drive.google.com/drive/folders/1zukMmnzy3XW3zuz7o6UQL2wRtaV2UBkk?usp=sharing'),
    ('Class Notes', 'https://docs.google.com/document/d/1LYqjvlBocqFYnEMH3uzXE6r_WK2KfaDFB8swgh33K9M/edit?usp=sharing')
    )

LANDING_PAGE_TITLE = "Welcome to " + SITENAME