from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from E_R_P_students.models import students
import json


# STUDENT LOGIN
def STUDENT_LOGIN_FUN(request):
    if(request.method=="POST"):
        print(json.loads(request.body))
        data=json.loads(request.body)
        USER_NAME=data['USER_NAME']
        PASSWORD=data['PASSWORD']
        num=students.objects.filter(USER_NAME=USER_NAME,PASSWORD=PASSWORD).exists()
        if(num): 
            user=students.objects.filter(USER_NAME=USER_NAME,PASSWORD=PASSWORD).values()
            return JsonResponse(list(user),safe=False)
        else:
            return JsonResponse("wrong credentials",safe=False)
    



# CHANGE STUDENT PASSWORD
def CHANGE_STUDENT_PASSWORD(request):
    if request.method=="POST":
        data=json.loads(request.body)
        USER_NAME=data['USER_NAME']
        PASSWORD=data['PASSWORD']
        students.objects.filter(USER_NAME=USER_NAME).update(PASSWORD=PASSWORD)     
        return JsonResponse("password updated successfully",safe=False)
    
# STUDENT ALL DATA  
  
def STUDENT_DATA(request):
    if request.method=='POST':
        data=json.loads(request.body)
        USER_NAME=data['USER_NAME']
        users=students.objects.filter(USER_NAME=USER_NAME).values()      
        return JsonResponse(list(users),safe=False)    

# UPDATE STUDEMT PROFILE

def UPDATE_STUDENT_PROFILE(request):
    if request.method=='POST':
        data=json.loads(request.body)
        USER_NAME=data['USER_NAME']
        father_name=data['father_name']
        email=data['email']
        phone_no=data['phone_no'] 
        students.objects.filter(USER_NAME=USER_NAME).update(father_name=father_name,email=email,phone_no=phone_no)
        return JsonResponse('success updation',safe=False)


