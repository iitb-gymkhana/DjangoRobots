# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SECRET'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Email server settings
EMAIL_HOST = "smtp-auth.iitb.ac.in"
EMAIL_PORT = 25

EMAIL_HOST_USER = ""

EMAIL_HOST_PASSWORD = ""

# Email Id which will appear in From header in email
EMAIL_FROM = ""

EMAIL_BACKEND = "core.notification.IITBEmailBackend"

SERVER_EMAIL = ""

EMAIL_SUBJECT_PREFIX = '[Django Robots]'

ADMINS = (
    ('Nautatva Navlakha', 'nnautatva@gmail.com'),
)

# DATABASES
# Define databases here to override default Databases.


# Settings for 'robots' app
""" By default a Sitemap statement is automatically added to the resulting robots.txt by reverse matching the URL of the installed Sitemap contrib app. This is especially useful if you allow every robot to access your whole site, since it then gets URLs explicitly instead of searching every link.

To change the default behaviour to omit the inclusion of a sitemap link, change the ROBOTS_USE_SITEMAP setting"""
ROBOTS_USE_SITEMAP = False


""" In case you want to use specific sitemap URLs instead of the one that is automatically discovered, change the ROBOTS_SITEMAP_URLS setting"""
# ROBOTS_SITEMAP_URLS = [
#     'http://www.example.com/sitemap.xml',
# ]


""" Inform django-robots about the view name of the sitemap instance (in urls.py) by 'ROBOTS_SITEMAP_VIEW_NAME' setting 

# Also use ROBOTS_SITEMAP_VIEW_NAME if you use custom sitemap views (e.g.: wagtail custom sitemaps)."""
# ROBOTS_SITEMAP_VIEW_NAME = 'cached-sitemap'


""" By default a Host statement is automatically added to the resulting robots.txt to avoid mirrors and select the main website properly.

To change the default behaviour to omit the inclusion of host directive, change the ROBOTS_USE_HOST setting """
# ROBOTS_USE_HOST = False


"""if you want to prefix the domain with the current request protocol(http or https as in Host: https: // www.mysite.com) add this setting:
"""
# ROBOTS_USE_SCHEME_IN_HOST = True


""" You can optionally cache the generation of the robots.txt. Add or change the ROBOTS_CACHE_TIMEOUT setting with a value in seconds in your Django settings file. By default, the value is None
"""
# ROBOTS_CACHE_TIMEOUT = 60*60*6


""" ____ """
# ROBOTS_SITE_BY_Request
