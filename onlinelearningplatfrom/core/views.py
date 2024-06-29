from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile, Course, Lessons, Enrollment, Progress
from .forms import ProfileForm, CourseForm, LessonForm
from django.db.models import Count

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
    form = CourseForm(instance=courses)
    lesson_list = Lessons.objects.filter(course=courses)
    lesson_form = LessonForm(course=courses)
    lesson_forms = [LessonForm(instance=lesson) for lesson in lesson_list]
    context = {'courses': courses, 'form': form, 'lesson_forms': lesson_forms, 'lesson_form': lesson_form, 'lesson_list': lesson_list}
    return render(request, 'instructor/view_course.html', context)

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
def updatecourse(request, pk):
    courses = Course.objects.get(id=pk)
    lesson_form = LessonForm(course=courses)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, user=request.user, instance=courses)
        if form.is_valid():
            form.save()
            return redirect('courseview', pk=courses.id)
    else:
        form = CourseForm(user=request.user, instance=courses)
    
    context = {'courses': courses, 'form': form, 'lesson_form': lesson_form}
    return render(request, 'instructor/view_course.html', context)

@login_required(login_url='loginpage')
def deletecourse(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return redirect('inshome')

@login_required(login_url='loginpage')
def addlesson(request, pk):
    courses = Course.objects.get(id=pk)
    form = CourseForm(instance=courses)
    if request.method == 'POST':
        lesson_form = LessonForm(request.POST, course=courses)
        if lesson_form.is_valid():
            lesson_form.save()
            return redirect('courseview', pk=courses.id)
    else:
        lesson_form = LessonForm(course=courses)
    context = {'courses': courses, 'form': form, 'lesson_form': lesson_form}
    return render(request, 'instructor/view_course.html', context)

@login_required(login_url='loginpage')
def updatelesson(request, pk, lesson_pk):
    courses = Course.objects.get(id=pk)
    less = Lessons.objects.get(id=lesson_pk)
    lesson_list = Lessons.objects.filter(course=courses)
    form = CourseForm(user=request.user, instance=courses)
    if request.method == 'POST':
        lesson_form = LessonForm(request.POST, course=courses, instance=less)
        if lesson_form.is_valid():
            lesson_form.save()
            return redirect('courseview', pk=pk)
    else:
        lesson_form = LessonForm(course=courses, instance=less)
    context = {'courses': courses, 'form': form, 'lesson_form': lesson_form, 'lesson_list': lesson_list}
    return render(request, 'instructor/view_course.html', context)

@login_required(login_url='loginpage')
def deletelesson(request, pk, lesson_pk):
    lesson = Lessons.objects.get(id=lesson_pk)
    lesson.delete()
    return redirect('courseview', pk=pk)

# Student Part
@login_required(login_url='loginpage')
def stuhomepage(request):
    courses = Course.objects.annotate(enrollment_count=Count('enrollment'))
    return render(request, 'students/student_home.html', {'courses': courses})

@login_required(login_url='loginpage')
def previewcourse(request, pk):
    courses = Course.objects.get(id=pk)
    is_enrolled = Enrollment.objects.filter(student=request.user, course=courses).exists()
    total_enrollments = Enrollment.objects.filter(course=courses).count()
    context = {'courses': courses, 'is_enrolled': is_enrolled, 'total_enrollments': total_enrollments}
    return render(request, 'students/preview.html', context)

@login_required(login_url='loginpage')
def enrollcourse(request, pk):
    courses = Course.objects.get(id=pk)
    enrollment, created = Enrollment.objects.get_or_create(student=request.user, course=courses)
    if created:
        lessons = Lessons.objects.filter(course=courses)
        for l in lessons:
            Progress.objects.create(enrollment=enrollment, lesson=l)
        return redirect('mycourses')   
    else:
        return redirect('previewcourse', pk=pk) 
    

@login_required(login_url='loginpage')
def mycourses(request):
    enrolments = Enrollment.objects.filter(student=request.user)
    courses = [enrolled.course for enrolled in enrolments]
    enr = [enrolled.completion_status for enrolled in enrolments]
    combined = zip(courses, enr)
    return render(request, 'students/my_courses.html', {'combined': combined})

@login_required(login_url='loginpage')
def mycoursepreview(request, pk):
    courses = Course.objects.get(id=pk)
    enrollment = Enrollment.objects.get(student=request.user, course=courses)
    progess_list = Progress.objects.filter(enrollment=enrollment)
    lessons = [p.lesson for p in progess_list]
    combined = zip(lessons, progess_list)
    total_lesson = Progress.objects.filter(enrollment=enrollment).count()
    completed_lesson = Progress.objects.filter(enrollment=enrollment, completed=True).count()
    progress = (completed_lesson/total_lesson)*100
    if progress == 100.0:
        enrollment.completion_status = True
        enrollment.save()
    context = {'courses': courses, 'lessons': lessons, 'combined': combined, 'progress': progress}
    return render(request, 'students/my_course_preview.html', context)

@login_required(login_url='loginpage')
def markcomplete(request, pk, lesson_pk):
    courses = Course.objects.get(id=pk)
    lessons = Lessons.objects.get(id=lesson_pk)
    enrollment = Enrollment.objects.get(student=request.user, course=courses)
    progress = Progress.objects.get(enrollment=enrollment, lesson=lessons)
    progress.completed = True
    progress.save()
    return redirect('mycoursepreview', pk=pk)


