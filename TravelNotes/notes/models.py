from django.conf import settings
from django.db import models
from django.utils import timezone
from enum import Enum


class Note(models.Model):
	# class TagChoices(Enum):
	# 	Weekend = "Weekend Break"
	# 	Short = "Short Term"
	# 	Long = "Long Term"
	# 	Gap = "Gap Year"

	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	cover = models.ImageField(upload_to = 'images/', default = '/images/default.jpeg')
	tag = models.CharField(max_length = 20, default='Weekend Break')

	def __str__(self):
		return self.title