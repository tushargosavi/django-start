from django import forms
from django.contrib.auth.models import User

CHOICES = (('1', '5-10 Years',), ('2', '10-15 Years'))
CITIES = (('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Pune', 'Pune'))

# Create your models here.
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput()
    )
    ageGroup = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    city = forms.ChoiceField(choices=CITIES)

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2

        raise forms.ValidationError("Password do not match")

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise forms.ValidationError("User already exists")
