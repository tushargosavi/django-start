from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from registration.forms import RegisterForm
from registration.models import UserProfile


def home(request):
    return render(request, 'home.html')


def save_user_info(form):
    username = form.cleaned_data['username']
    email = form.cleaned_data['email']
    passwd = form.cleaned_data['password1']
    ageGroup = form.cleaned_data['ageGroup']
    city = form.cleaned_data['city']
    print("user " + username + " email " + email + " password " + passwd + " age " + ageGroup + " city " + city)

    user = User.objects.create_user(username, email=email, password=passwd)
    user.save()
    prof = UserProfile(user=user, city=city, ageGroup=ageGroup)
    prof.save()

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            save_user_info(form)
            return HttpResponseRedirect("/regsuccess")
    else:
        form = RegisterForm()

    return render(request, 'registration/registration.html', {
        'form':form
    })


def regsuccess(request):
    return render_to_response('registration/regsuccess.html')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")

