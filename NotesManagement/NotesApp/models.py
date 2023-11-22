from django.db import models

# Create your models here.

class Student(models.Model):
	name=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	email=models.CharField(max_length=30,unique=True)

class Notes(models.Model):
	sid=models.IntegerField()
	sub=models.CharField(max_length=100)
	note=models.CharField(max_length=10000)
	like=models.IntegerField()
	dislike=models.IntegerField()

class Requests(models.Model):
	sname=models.CharField(max_length=50)
	rid=models.IntegerField()
	sub=models.CharField(max_length=50)
	atid=models.IntegerField()
	ntid=models.IntegerField()

class Accepted(models.Model):
	rid=models.IntegerField()
	nid=models.IntegerField()
	s_sub=models.CharField(max_length=50)
	s_note=models.CharField(max_length=10000)