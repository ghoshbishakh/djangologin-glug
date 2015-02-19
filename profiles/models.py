from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):

    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,

    )

    mobile = models.CharField(
        max_length=12,

    )

    address = models.CharField(
        max_length=255,

    )

    owner = models.ForeignKey(User)

    def __str__(self):

        return ' '.join([
            self.first_name,
            self.last_name,
        ])

# Create your models here.
