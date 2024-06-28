from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request, user)
            user_profile = Profile.objects.get(user=user)
            user_role = user_profile.role
            if user_role == 'instructor':
                return redirect('inshome')
            else:
                return redirect('stuhome')
    return render(request, 'auth/login.html')

def logout_user(request):
    logout(request)
    return redirect('loginpage')

def regeister_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('loginpage')
    else:
        form = UserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'auth/register.html', {'form': form, 'profile_form': profile_form})

@login_required(login_url='loginpage')
def inshomepage(request):
    return render(request, 'instructor/instructor_home.html')

@login_required(login_url='loginpage')
def stuhomepage(request):
    return render(request, 'students/student_home.html')

