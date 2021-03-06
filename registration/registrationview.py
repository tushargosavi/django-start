from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from forms import RegisterForm
from models import UserProfile

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


def checkuser(request):
    userName = request.GET['username']
    result="available"
    try:
        user = User.objects.get_by_natural_key(userName)
        print(user)
        result="taken"
    except:
        pass
    return HttpResponse(result)
