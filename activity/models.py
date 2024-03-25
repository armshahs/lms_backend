import uuid
from django.db import models
from django.contrib.auth.models import User
from course.models import Course, Lesson


# Create your models here.
class Activity(models.Model):

    STARTED = "started"
    DONE = "done"

    STATUS_CHOICES = (
        (STARTED, "Started"),
        (DONE, "Done"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(
        Course, related_name="activities", on_delete=models.CASCADE
    )
    lesson = models.ForeignKey(
        Lesson, related_name="activities", on_delete=models.CASCADE
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STARTED)
    created_by = models.ForeignKey(
        User, related_name="activities", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        return (
            str(self.created_by)
            + " || "
            + self.status
            + " || "
            + str(self.course)
            + " || "
            + str(self.lesson)
        )
