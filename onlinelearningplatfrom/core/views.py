from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile, Course
from .forms import ProfileForm, CourseForm

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
    courses = Course.objects.filter(user=request.user)
    return render(request, 'instructor/instructor_home.html', {'courses': courses})

@login_required(login_url='loginpage')
def viewcourse(request, pk):
    courses = Course.objects.get(id=pk)
    return render(request, 'instructor/view_course.html', {'courses': courses})

@login_required(login_url='loginpage')
def addcourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('inshome')
    else:
        form = CourseForm(user=request.user)
    
    return render(request, 'instructor/add_course.html', {'form': form})

@login_required(login_url='loginpage')
def stuhomepage(request):
    return render(request, 'students/student_home.html')



