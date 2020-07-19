from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from E_R_P_students.models import teacher,students,quires
import json

# STUDENT LOGIN

def TEACHER_LOGIN_FUN(request):
    if(request.method=="POST"):
        data=json.loads(request.body)
        USER_NAME=data['USER_NAME']
        PASSWORD=data['PASSWORD']
        num=teacher.objects.filter(USER_NAME=USER_NAME,PASSWORD=PASSWORD).exists()
        if(num):          
            return JsonResponse("logged in",safe=False)
        else:
            return JsonResponse("wrong credentials",safe=False)
        
# Create your views here.

# FOR INSERT NEW STUDENT

def INSERT_NEW_STUDENT(request):
    
    if request.method=='POST':
        data=json.loads(request.body)
        USER_NAME=data['USER_NAME']
        father_name=data['father_name']
        email=data['email']
        branch=data['branch']
        phone_no=data['phone_no']
        num_results = students.objects.filter(USER_NAME=USER_NAME).exists()
        
        if(num_results):
            data="Student already exists"
            return JsonResponse(data,safe=False)
        else:                                   
            students.objects.create(USER_NAME=USER_NAME,father_name=father_name,email=email,branch=branch,phone_no=phone_no)
            quires.objects.create(USER_NAME=USER_NAME)
            data="Student inserted"
            return JsonResponse(data,safe=False)



# UPDATE STUDENT PROFILE 


def UPDATE_SUDENT_PROFILE(request):
    if request.method=='POST':
        data=json.loads(request.body)
        USER_NAME=data['USER_NAME']
        father_name=data['father_name']
        email=data['email']
        branch=data['branch']
        phone_no=data['phone_no'] 
        students.objects.filter(USER_NAME=USER_NAME).update(father_name=father_name,email=email,branch=branch,phone_no=phone_no)
        return JsonResponse('success updation',safe=False)


# SHOW ALL ACTIVE STDENT

def ALL_ACTIVE_STUDENT(request):
    if request.method=='GET':
        users=students.objects.filter(ACTIVE_STATUS="ACTIVE").values()
        return JsonResponse(list(users),safe=False)
    
    
    


# INACTIVE STDENT FROM DATABASE       (DELETE)       
        
def STUDENT_INACTIVE_FUN(request):
    if request.method=='POST':        
        print(json.loads(request.body))
        data=json.loads(request.body)
        USER_NAME=data['USER_NAME']
        print(USER_NAME)
        students.objects.filter(USER_NAME=USER_NAME).update(ACTIVE_STATUS="INACTIVE")
        quires.objects.filter(USER_NAME=USER_NAME).update()   
        return JsonResponse('Item succsesfully delete!',safe=False)



