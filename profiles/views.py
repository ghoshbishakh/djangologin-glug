from django.shortcuts import render
from forms import UserForm
from forms import CreateUserForm


def home(request):
    return render(request, 'profiles/home.html')


def update_user(request, template_name="profiles/update_user.html"):
    if request.method == "POST":
        form = UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return render(request, 'profiles/home.html')
    else:
        form = UserForm(data=request.POST, instance=request.user)
    return render(request, 'profiles/update_user.html', {'form': form})


def create_user(request, template_name="profiles/create_user.html"):
    if request.method == "POST":
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            form.clean_username()
            form.clean()
            form.save()
            return render(request, 'profiles/home.html')
    else:
        form = CreateUserForm(data=request.POST)
    return render(request, 'profiles/create_user.html', {'form': form})
# Create your views here.
# Create your views here.
