from django.db import models
from django.utils import timezone

class Question(models.Model):
    field = models.CharField(max_length=500)
    question =  models.CharField(max_length=500)
    createAt = models.DateTimeField(default=timezone.now)

class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    results = models.IntegerField(default=0,null=True)
    percentage = models.DecimalField(default=0, max_digits=8, decimal_places=2,null=True)
    createAt = models.DateTimeField(default=timezone.now)

