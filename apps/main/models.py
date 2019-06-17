# Django
from django.db import models

class Client (models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identifaction = models.IntegerField(unique = True)

    def __str__(self):
        return self.name


class Account (models.Model):
    bank = models.CharField(max_length=50)
    create_date = models.DateField(auto_now=True)
    balance = models.IntegerField(default=0, blank = False)

    def __str__(self):
        return str(self.bank)


class Profile (models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class Transaction (models.Model):
    commerce = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, related_name='transactions', on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return self.commerce