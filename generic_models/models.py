from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Animal(models.Model):

    name = models.CharField(max_length=100)

    def make_sound(self):

        raise NotImplementedError()


class Dog(Animal):

    def make_sound(self):

        return "guau!"


class Cat(Animal):

    def make_sound(self):

        return "meow!"


class AnimalHouse(models.Model):
    
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    
    animal = generic.GenericForeignKey('content_type', 'object_id')
