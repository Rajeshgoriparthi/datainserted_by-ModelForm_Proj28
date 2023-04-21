from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=30)

    def __str__(self):
        return self.topic_name

class Gender(models.Model):
    gender=models.CharField(max_length=30)

    def __str__(self):
        return self.gender

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    adress=models.CharField(max_length=100)
    gender=models.ForeignKey(Gender,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
