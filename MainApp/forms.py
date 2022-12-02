from django import forms

from .models import *

#to build it in same pattern of our models defined
class TopicForm(forms.ModelForm):
    #add custom fields here after this derive from our model
    class Meta:
        model = Topic
        fields =['text']
        labels = {'text':'Topic Name'}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields =['text']
        labels = {'text':'Enter Entry here:'}

        widgets = {'text':forms.Textarea(attrs={'cols':80})}