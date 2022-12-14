from django.shortcuts import render,redirect
from .models import *
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

#post or get --> request
#Request is an httprequest object
def index(request):
    return render(request,'MainApp/index.html')


@login_required
def topics(request):
    #order based om when it was created
    #add minus in fromt of attribute ('-date_added')
    #topics= Topic.objects.order_by('date_added')
    #topics that belong to the user, check if 
    topics= Topic.objects.filter(owner=request.user).order_by('date_added')


    #use a dict to pass in render func --> pass data from db to template
    #key --> is the smae var name we use in our template file eg --> topics.html, value that should match the object name in view.py
    context = {'topics':topics}

    #to display a page with data in it
    return render(request,'MainApp/topics.html',context)

@login_required
def topic(request,topic_id):

    t = Topic.objects.get(id=topic_id)

    #check if the owner of the topic is the current person requesting that page
    if t.owner != request.user:
        raise Http404
    #entries related to that specific topic
    entries = Entry.objects.filter(topic=t)

    context = {'topic':t,'entries':entries}

    return render(request,'MainApp/topic.html',context)

@login_required
#evaluate type of request
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        print(request.POST)
        form = TopicForm(data=request.POST)
        #validation
        if form.is_valid():
            new_topic= form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            #automatically go to another page
            return redirect('MainApp:topics')

    context = {'form':form}
    return render(request, 'MainApp/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm()
    else:
        #print(request.POST)
        form = EntryForm(data=request.POST)
        #validation
        if form.is_valid():
            #since it dnt have id , we shouldnt commit it
            new_entry = form.save(commit=False)
            #get the topic first from 52
            new_entry.topic = topic
            new_entry.save()
            #automatically go to another page
            return redirect('MainApp:topic',topic_id=topic_id)

    context = {'form':form,'topic':topic}
    return render(request, 'MainApp/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic # we are getting this topic from our entry model

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #load the that specfic entry to the textbox
        form = EntryForm(instance=entry)
    else:
        form = EntryForm (instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('MainApp:topic',topic_id=topic.id)

    context = {'form':form,'topic':topic,'entry':entry}
    return render(request, 'MainApp/edit_entry.html',context)