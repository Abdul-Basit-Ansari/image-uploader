from django.db import models

# Create your models here.
class Image(models.Model):
	sno = models.AutoField(primary_key=True)
	image = models.ImageField(upload_to="myimage")
	date = models.DateTimeField(auto_now_add=True)


	# def __str__(self):
	# 	return self.date