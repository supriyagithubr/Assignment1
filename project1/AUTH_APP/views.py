from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def registerview(request):
    form = UserCreationForm()
    template_name = 'AUTH_APP/register.html'
    context = {'form': form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginform_url')
    return render(request, template_name, context)

def loginview(request):
    template_name = 'AUTH_APP/loginform.html'
    context = {}
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
       # print(un,'------', pw)

        user = authenticate(username=un, password=pw)
        #print(user)
        if user is not None:
            login(request, user)
            return redirect('showorder_url')
    return render(request, template_name, context)


def logoutview(request):
    logout(request)
    return redirect('loginform_url')

