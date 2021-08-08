from django.db import models

# Create your models here.
class register_students(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    ID_card = models.CharField(max_length=13)
    birthdate = models.DateTimeField
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    passcode = models.CharField(max_length=5)

    def __str__(self):
        #return '<Name : %s>' % self.name
        return self.name+' '+self.lastname+' '+self.email+' '+self.gender
