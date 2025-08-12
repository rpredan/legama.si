from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import Lower

# Create your models here.
class CustomUser(AbstractUser):
    # email je obvezen in unikaten
    email = models.EmailField("email address", unique=True)

    # dodatna polja (po potrebah)
    institution = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
    
    class Meta:
        constraints = [
            # case-insensitive unikatnost (PostgreSQL)
            models.UniqueConstraint(Lower("email"), name="uniq_ci_email"),
        ]