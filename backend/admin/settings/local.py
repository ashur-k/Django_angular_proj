from .base import *
from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default='django-insecure-)18iw!^899@v)_((9-jbud$q%0ijhz%nqvnj$38b(0+9op!s)m'
)

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']