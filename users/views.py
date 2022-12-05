from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        #validation
        if form.is_valid():
            #since it dnt have id , we shouldnt commit it
            new_user = form.save()
            #allow user to login same time
            login(request, new_user)

            return redirect('MainApp:index')

    context = {'form':form}
    return render(request, 'registration/register.html',context)
    
