from django.db import models

# Create your models here.
class Person(models.Model):
    id=models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=10)
    Email_id = models.EmailField(max_length=15)
    phone_number = models.IntegerField()
    Address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Name
