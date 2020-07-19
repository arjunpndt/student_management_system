from django.db import models

    
    
class teacher(models.Model):
    USER_NAME = models.CharField(max_length=200,default="")
    PASSWORD=models.CharField(max_length=250,default="KIET123")   
   


class students(models.Model):
    USER_NAME=models.CharField(max_length=250,unique=True,default="NULL")
    PASSWORD=models.CharField(max_length=250,default="KIET123")
    father_name=models.CharField(max_length=250,default="father")
    father_name=models.CharField(max_length=250,default="father")
    email=models.CharField(max_length=250,unique=True,default="kiet123@.com")
    branch=models.CharField(max_length=250,default="IT")
    phone_no=models.BigIntegerField(unique=True,default="1234567890")
    STATUS=models.CharField(max_length=100,default="NO QUERY")
    ACTIVE_STATUS=models.CharField(max_length=100,default="ACTIVE")
    
   
    
class quires(models.Model):
    # query=models.ForeignKey(students,null=True,on_delete=models.CASCADE)
    USER_NAME=models.CharField(max_length=250,default="NULL")
    date=models.DateTimeField(auto_now_add=True)
    STATUS=models.CharField(max_length=100,default="NO QUERY")
