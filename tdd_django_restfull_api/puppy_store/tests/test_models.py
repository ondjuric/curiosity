"""
Represents test cases for the Puppy model
"""
from django.test import TestCase
from puppy_store.models import Puppy


class PuppyTest(TestCase):
    """
    Test module for Puppy Model
    """

    def setUp(self):
        Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        Puppy.objects.create(
            name='Muffin', age=1, breed='Grandane', color='Brown')
    
    def test_puppy_breed(self):
        puppy_casper = Puppy.objects.get(name='Casper')
        puppy_maffin = Puppy.objects.get(name='Muffin')
        self.assertEqual(
            puppy_casper.get_breed(), "Casper belongs to Bull Dog breed."
        )
        self.assertEqual(
            puppy_maffin.get_breed(), "Muffin belongs to Grandane breed."
        )