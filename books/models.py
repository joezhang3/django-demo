from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=10)
    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=10)
    def __unicode__(self):
        return self.name
class Lim(models.Model):
    name = models.CharField(max_length=10)
    def __unicode__(self):
        return self.name

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Lim)


