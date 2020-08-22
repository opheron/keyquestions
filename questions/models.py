from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Question(models.Model):
    question_text = models.TextField()
    published_date = models.DateTimeField(null=True, blank=True)
    submitted_date = models.DateTimeField(default=timezone.now)
    # submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default='')
    attribution_url = models.TextField(blank=True, default="")
    attribution_text = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=3,
        choices=(("PUB", "Published"), ("REV", "In Review"), ("REM", "Removed")),
        default="REV",
    )

    def __str__(self):
        return self.question_text
