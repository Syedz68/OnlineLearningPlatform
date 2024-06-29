from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lessons, Enrollment, Progress

@receiver(post_save, sender=Lessons)
def update_progress_for_new_lesson(sender, instance, created, **kwargs):
    if created:
        # Get all enrollments for the course of the new lesson
        enrollments = Enrollment.objects.filter(course=instance.course)
        
        # Create a new progress entry for each enrollment
        for enrollment in enrollments:
            Progress.objects.create(
                enrollment=enrollment,
                lesson=instance,
                completed=False
            )
