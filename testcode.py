import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django
django.setup()

from MainApp.models import *

#select everthing Topic --> eq to select *
topics = Topic.objects.all()

#query set object #--> while querying the db return objects from the string text that we returned from model.py
print(topics)

#object is iterable
#text is an attribute of the object
for t in topics:
    print(t.text)
    print(t.date_added)
    print(t.id)

#where id =1 , all attributes attached to the object can be accessed
topic = Topic.objects.get(id=1)
print(topic)
print(topic.date_added)
print(topic.text)

#where id>1 and id<5
#topic.objects.filter(id_gte 1 and id_lte 5)

#get all entries related to that specific topic
entries = topic.entry_set.all()

#or where topic = 
entries = Entry.objects.filter(topic=t)
entries = Entry.objects.filter(topic=2)


#or
for e in entries:
    print(e)
    print(e.text)


#to access user models 
from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username,user.id)





