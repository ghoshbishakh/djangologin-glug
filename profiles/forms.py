from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email']


class CreateUserForm(UserCreationForm):
    pass
