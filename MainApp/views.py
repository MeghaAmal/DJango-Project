from django.shortcuts import render
from .models import *

# Create your views here.

#post or get --> request
def index(request):
    return render(request,'MainApp/index.html')

def topics(request):
    #order based om when it was created
    #add minus in fromt of attribute ('-date_added')
    topics= Topic.objects.order_by('date_added')

    #use a dict to pass in render func --> pass data from db to template
    #key --> is the smae var name we use in our template file eg --> topics.html, value that should match the object name in view.py
    context = {'topics':topics}

    #to display a page with data in it
    return render(request,'MainApp/topics.html',context)


def topic(request,topic_id):

    t = Topic.objects.get(id=topic_id)
    #entries related to that specific topic
    entries = Entry.objects.filter(topic=t)

    context = {'topic':t,'entries':entries}

    return render(request,'MainApp/topic.html',context)


