AUTHOR = "sfiera"
SITENAME = "Recipes"
SITEURL = ""
SITELOGO = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
SITETITLE = "Recipes"
CUSTOM_CSS = "static/custom.css"

THEME = "./flex"
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISABLE_URL_HASH = True
COPYRIGHT_NAME = "sfiera"
CC_LICENSE = { "name": "CC-BY License", "version": "4.0", "slug": "by" }

PATH = "content"

TIMEZONE = "Asia/Tokyo"

DEFAULT_LANG = "en"

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_PATHS = [""]
ARTICLE_PATHS = []
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
STATIC_PATHS = ["static", "images"]
INDEX_SAVE_AS = ''

# Blogroll
LINKS = [
        ('About', '/about'),
        ('Metric', '/metric'),
]

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
