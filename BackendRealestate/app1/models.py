from django.db import models


# Create your models here.
class Rental(models.Model):
    houseName = models.CharField(max_length=120)
    area = models.CharField(max_length=120)
    streetName = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    address = models.TextField()
    location = models.URLField()
    ownerName = models.CharField(max_length=120)
    ownerEmail = models.EmailField()
    rent = models.DecimalField(max_length=15, max_digits=20, decimal_places=5)
    images = models.ImageField(upload_to='rental/')

    def __str__(self):
        return f"{0} {1} {2}".format(self.houseName,self.area,self.city)


class User(models.Model):
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return self.email


class Admins(models.Model):
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    email = models.EmailField()
    ownerCode = models.IntegerField()
    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=120)
    message = models.TextField()
    email = models.EmailField()
    def __str__(self):
        return self.email

class Issues(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    issue = models.TextField()
    images=models.ImageField(upload_to='complaints/')

    def __str__(self):
        return self.issue