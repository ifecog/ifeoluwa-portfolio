from django.db import models
from datetime import datetime

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=80)
    display_photo = models.ImageField(upload_to='display_photo/')
    about_photo = models.ImageField(upload_to='about_photo/')
    body = models.TextField()
    resume = models.FileField(upload_to='documents/', null=True)
    city = models.CharField(max_length=30, default=False)
    country = models.CharField(max_length=30, default=False)
    phone_number = models.CharField(max_length=18, default=False)
    email = models.EmailField(max_length=254, default=False)
    github_link = models.URLField(max_length=100)
    linkedin_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Skill(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    TYPE_CHOICES = (
        ('personal', 'Personal'),
        ('contributions', 'Contributions')
    )
    
    name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='projects/')
    web_url = models.URLField(max_length=100, null=True, blank=True)
    github_url = models.URLField(max_length=100, null=True, blank=True)
    description = models.TextField()
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='personal')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name