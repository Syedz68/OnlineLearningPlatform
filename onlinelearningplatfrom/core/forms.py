from django.forms import ModelForm
from .models import Profile, Course


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['role']

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'cover']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CourseForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(CourseForm, self).save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance