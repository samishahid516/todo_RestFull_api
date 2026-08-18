from django.db import models

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Todo(TimeStamp):
    title = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    