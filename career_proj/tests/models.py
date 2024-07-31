from django.db import models
from django.contrib.auth.models import User

class Tests(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)

class Question(models.Model):
    SECTION_CHOICES = (
        ('logical_reasoning', 'Logical Reasoning'),
        ('numerical_ability', 'Numerical Ability'),
        ('verbal_ability', 'Verbal Ability'),
    )
    text = models.CharField(max_length=200)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    section = models.CharField(max_length=50)

