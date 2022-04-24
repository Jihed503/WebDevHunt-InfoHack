from django.db import models

# Create your models here.

class Client(models.Model):
    # id_client = 
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    zip = models.IntegerField()
    place = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.IntegerField()

class Technologie(models.Model):
    name = models.CharField(max_length=50)


class Developer(models.Model):
    # id_client = 
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    zip = models.IntegerField()
    place = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.IntegerField()
    position = models.CharField(max_length=50)
    about = models.CharField(max_length=500, default='')
    image = models.CharField(max_length=500, default='https://rouelibrenmaine.fr/wp-content/uploads/2018/10/empty-avatar.png')
    technologies = models.ManyToManyField(Technologie)

class Project(models.Model):
    id_dev = models.ForeignKey(Developer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=500, default='https://www.projz.com/static/media/screenshot1.d9c4e990.png')
    github = models.CharField(max_length=500, default='https://github.com')

class Reply(models.Model):
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=5)


    
