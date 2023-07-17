from django.db import models


class Task(models.Model):
	title = models.CharField(max_length=255)
	completed = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return str(self.title)