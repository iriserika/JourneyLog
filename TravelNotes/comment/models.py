from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
	note = models.ForeignKey("notes.Note", on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	comment = models.TextField()
	comment_date = models.DateTimeField(default=timezone.now)

