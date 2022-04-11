# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_vf-!)t^rgkg9mb980qr++6cyesgbt3q=uwrt#n0i8jpwrjta9'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bbooing',
        'USER': 'root',
        'PASSWORD': 'abcd1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
     	'OPTIONS': {'charset': 'utf8mb4'}
    }
}