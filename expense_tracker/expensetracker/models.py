from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Base model for User and Admin (Common Fields)
class Person(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        abstract = True  # This makes Person a base class for other models

# User model
class User(Person):
    # You can add more fields specific to User here if necessary
    def __str__(self):
        return self.full_name

# Admin model
class Admin(Person):
    # You can add more fields specific to Admin here if necessary
    def __str__(self):
        return self.full_name

# Transaction model (User has a relation with Transaction)
class Transaction(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')

    def __str__(self):
        return self.title

# Log model (User and Admin have a relationship with Log)
class Log(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Log entry for {self.content_object} on {self.date}"

