from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Reuseable state model
class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StateAssignment(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ('state', 'content_type', 'object_id')


# model for hostpital , physician , nurse , telemedicine , visa , contact
class HosFile(models.Model):
    file = models.FileField(upload_to='hospital/')

class Hospital(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    resumes = models.ManyToManyField(HosFile)

    def __str__(self):
        return self.fullname

class PhyFile(models.Model):
    file = models.FileField(upload_to='physician/')

class Physician(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    resumes = models.ManyToManyField(PhyFile)

    def __str__(self):
        return self.fullname

class NurFile(models.Model):
    file = models.FileField(upload_to='Nurses/')

class Nurse(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    resumes = models.ManyToManyField(NurFile)
    
    def __str__(self):
        return self.fullname

'''
class TeleFile(models.Model):
    file = models.FileField(upload_to='telemedicines/')
class Telemedicines(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    resumes = models.ManyToManyField(TeleFile)
    
    def __str__(self):
        return self.fullname

class VisaFile(models.Model):
    file = models.FileField(upload_to='visas/')
class Visa(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    resumes = models.ManyToManyField(VisaFile)
    
    def __str__(self):
        return self.fullname
    '''

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    
    def __str__(self):
        return self.fullname