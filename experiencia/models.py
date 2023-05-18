from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Questionario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    how_you_find_us = models.CharField(max_length=30)
    about_our_location = models.CharField(max_length=56)
    About_organization_space = models.CharField(max_length=256)
    waitin_time = models.CharField(max_length=256)
    about_our_employees = models.CharField(max_length=256)
    about_our_service = models.CharField(max_length=256)
    do_you_intend_to_return = models.CharField(max_length=256)
    criticize_or_praise = models.CharField(max_length=500)