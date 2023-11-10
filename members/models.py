from django.db import models

class Functie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    function = models.ForeignKey(Functie, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
