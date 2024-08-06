from django.db import models

# Create your models here.
class User(models.Model):
    STATUS_CHOICES= [
        ('ACTIVE', 'Active'),
        ('BLOCKED', 'Blocked'),
        ('DELETED', 'Deleted'),
        ('IN_ACTIVE', 'Inactive'),
    ]
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='IN_ACTIVE')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.username