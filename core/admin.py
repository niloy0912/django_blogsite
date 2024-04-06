from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Blog)
admin.site.register(Author)

# admin cred:
#   username: user
#   pass: 123