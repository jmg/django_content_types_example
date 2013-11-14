"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from models import Cat, Dog, AnimalHouse


class GenericsTest(TestCase):

    def setUp(self):

        self.mew = Cat(name="mew")
        self.mew.save()

        self.snoopy = Dog(name="snoopy")
        self.snoopy.save()

        cat_house = AnimalHouse(animal=self.mew)
        cat_house.save()

        dog_house = AnimalHouse(animal=self.snoopy)
        dog_house.save()

    def test_polymorphic_calls(self):

        houses = AnimalHouse.objects.all()

        self.assertEquals(houses[0].animal.make_sound(), "meow!")
        self.assertEquals(houses[1].animal.make_sound(), "guau!")

    def test_generic_filter(self):        

        cat_houses = AnimalHouse.objects.filter(content_type=ContentType.objects.get_for_model(Cat))
        self.assertEquals([house.animal for house in cat_houses], [self.mew])

        dog_houses = AnimalHouse.objects.filter(content_type=ContentType.objects.get_for_model(Dog))
        self.assertEquals([house.animal for house in dog_houses], [self.snoopy])
        