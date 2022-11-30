from django.contrib import admin
#. means same directory
#from .models import Topic,Entry
from .models import *


# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)
