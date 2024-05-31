# applications/models.py
from django.db import models

class BursaryApplication(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    bursary_details = models.TextField()
    institution = models.CharField(max_length=100)  # Add default value

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# If you have another model called Allocation, define it here.
# Ensure that all models are defined before importing them elsewhere
class Allocation(models.Model):
    # Define the fields for the Allocation model here
    pass