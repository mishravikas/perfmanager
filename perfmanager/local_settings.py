DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'perfdb',
        'USER': 'perf_user',
        'PASSWORD': '',
        'HOST': 'database',
        'PORT': '',
    }
}

#For running without docker
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'perfmandb',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }
