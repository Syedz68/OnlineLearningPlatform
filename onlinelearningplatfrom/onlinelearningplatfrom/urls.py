"""
URL configuration for onlinelearningplatfrom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page,name='loginpage'),
    path('logout/', views.logout_user,name='logout'),
    path('register/', views.regeister_page,name='registerpage'),
    path('inshome/', views.inshomepage,name='inshome'),
    path('courseview/<str:pk>/', views.viewcourse,name='courseview'),
    path('courseview/update/<str:pk>/', views.updatecourse, name='updatecourse'),
    path('courseview/delete/<str:pk>/', views.deletecourse, name='deletecourse'),
    path('courseview/<str:pk>/addlesson', views.addlesson,name='addlesson'),
    path('courseview/<str:pk>/updatelesson/<str:lesson_pk>/', views.updatelesson,name='updatelesson'),
    path('courseview/<str:pk>/deletelesson/<str:lesson_pk>/', views.deletelesson,name='deletelesson'),
    path('courseadd/', views.addcourse,name='courseadd'),
    path('stuhome/', views.stuhomepage,name='stuhome'),
    path('previewcourse/<str:pk>/', views.previewcourse,name='previewcourse'),
    path('enrollcourse/<str:pk>/', views.enrollcourse,name='enrollcourse'),
    path('mycourses/', views.mycourses,name='mycourses'),
    path('mycoursepreview/<str:pk>/', views.mycoursepreview,name='mycoursepreview'),
    path('mycoursepreview/<str:pk>/markcomplete/<str:lesson_pk>/', views.markcomplete,name='markcomplete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)