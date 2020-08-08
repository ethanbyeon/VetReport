from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404

class Client(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Case(models.Model):

    client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_of_case = models.DateField(null=True)
    role = models.CharField(max_length=200, null=True)
    clinician = models.CharField(max_length=200, null=True)
    veterinary_clinic = models.CharField(max_length=200, null=True)
    key_words = models.CharField(max_length=200, null=True)
    diagnosis = models.CharField(max_length=200, null=True)
    name_of_animal = models.CharField(max_length=200, null=True)
    signalment = models.CharField(max_length=200, null=True)
    complaint = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True)
    resources = models.TextField(blank=True)
    files = models.FileField(upload_to='resource/files', null=True, blank=True)
    pictures = models.ImageField(upload_to='resource/pictures', null=True, blank=True)

    def __str__(self):
        return self.animal_name

    def delete(self, *args, **kwargs):
        self.files.delete()
        self.pictures.delete()
        super().delete(*args, **kwargs)
