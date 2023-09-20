from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models

class MissingPerson(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)  # Assuming a maximum of 15 digits for phone number
    aadhar_number = models.CharField(max_length=12, unique=True)  # Aadhar number is 12 digits and should be unique
    image = models.ImageField(upload_to='missing_persons/')  # Store images in a 'missing_persons' directory
    missing_from = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class Location(models.Model):
    missing_person = models.ForeignKey('MissingPerson', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  # Decimal field for latitude (adjust max_digits and decimal_places as needed)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  # Decimal field for longitude (adjust max_digits and decimal_places as needed)
    detected_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Location for {self.missing_person.first_name} {self.missing_person.last_name}"

    class Meta:
        ordering = ['-detected_at']  # Show the most recent locations first
