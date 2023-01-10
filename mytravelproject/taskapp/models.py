from django.db import models

# Create your models here.
class Change(models.Model):
    title=models.CharField(max_length=255)
    img=models.ImageField(upload_to='image')
    descrp=models.TextField()

    def __str__(self):
        return self.title
class team(models.Model):
    name=models.CharField(max_length=250)
    photo=models.ImageField(upload_to='image')
    profile=models.TextField()
    def __str__(self):
      return self.name
