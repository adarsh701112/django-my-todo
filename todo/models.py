from django.db import models

class User(models.Model):  # Class name should be PascalCase
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # EmailField for validation
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    profile = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # Corrected method name
        return self.name 