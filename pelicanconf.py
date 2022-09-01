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
LINKS = (('Contact Me', 'mailto:caladof@newschool.edu'),
         ('Personal Website', 'https:www.filipacalado.com'))

# Social widget
SOCIAL = (('Github', 'https://github.com/gofilipa/'),
          ('Twitter', 'https://twitter.com/Caladoscope'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

## FC EDITs: 


## Customizing the navbar

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# MENUITEMS = (
#     ('Course Schedule', 'cnl-fall-22/pages/course_schedule.html'),
#     ('Syllabus', '/pages/syllabus.html'),
#     ('Homework', '/pages/homework.html'),
#     ('Class Notes', 'https://docs.google.com/document/d/1LYqjvlBocqFYnEMH3uzXE6r_WK2KfaDFB8swgh33K9M/edit?usp=sharing')
#     )

LANDING_PAGE_TITLE = "Welcome to " + SITENAME

STATIC_PATHS = ['images', 'pdfs']