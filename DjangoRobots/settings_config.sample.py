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

