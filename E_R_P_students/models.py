from django.db import models

class Users(models.Model):
    USER_NAME = models.CharField(max_length=200)
    USERTYPE = models.CharField(max_length=250, default="S")
    PASSWORD=models.CharField(max_length=250,default="KIET123")
    # pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.USER_NAME


class students(models.Model):
    USER_NAME=models.CharField(max_length=250,default="NULL")
    PASSWORD=models.CharField(max_length=250,default="KIET123")
    father_name=models.CharField(max_length=250,default="father")
    father_name=models.CharField(max_length=250,default="father")
    email=models.CharField(max_length=250,unique=True,default="kiet123@.com")
    branch=models.CharField(max_length=250,default="IT")
    phone_no=models.BigIntegerField(unique=True,default="1234567890")
    STATUS=models.CharField(max_length=100,default="NO QUERY")
    
    def __str__(self):
        return self.USER_NAME
    
class queries(models.Model):
    query=models.ForeignKey(students,null=True,on_delete=models.CASCADE)
    USER_NAME=models.CharField(max_length=250,default="NULL")
    date=models.DateTimeField(auto_now_add=True)
    STATUS=models.CharField(max_length=100,default="NO QUERY")
