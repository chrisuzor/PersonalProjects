from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
<<<<<<< HEAD
    image = models.FilePathField(path="/img")
=======
    image = models.FilePathField(path='/img')
>>>>>>> 94a81eb432a52582e503668e85b4cc9249584108
