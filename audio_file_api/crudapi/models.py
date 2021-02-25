from django.db import models

# Create your models here.

class Song(models.Model):
	name = models.CharField(max_length=100)
	duration_in_number_of_seconds = models.IntegerField(default = 0)
	uploaded_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Podcast(models.Model):
	name = models.CharField(max_length=100)
	duration_in_number_of_seconds = models.IntegerField(default = 0)
	uploaded_time = models.DateTimeField(auto_now=True)
	host = models.CharField(max_length = 100)
	participant = models.CharField(max_length=1000, null =True,blank =True)

	def __str__(self):
		return self.name


class Audiobook(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	narrator = models.CharField(max_length=100)
	duration_in_number_of_seconds = models.IntegerField(default = 0)
	uploaded_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title