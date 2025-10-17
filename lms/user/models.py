from django.db import models

# Create your models here.
class user:
    USER_TYPE = {
        "S": "Student",
        "I": "Instructor",
        "A": "Admin",
    }
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=1, choices=USER_TYPE)  # e.g., 'student', 'instructor', 'admin'
    def __str__(self):
        return self.name