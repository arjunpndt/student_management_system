from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from E_R_P_students.models import students,quires
import json




# QUERY RAISE WHN TECHER INSERT NEW STUDENT 

def RAISE_STUDENT_QUERY(request):
    if request.method=="POST":        
        print(json.loads(request.body))
        data=json.loads(request.body)
        USER_NAME=data['USER_NAME']
        students.objects.filter(USER_NAME=USER_NAME).update(STATUS="PENDING")
        quires.objects.filter(USER_NAME=USER_NAME).update(STATUS="PENDING")
        return JsonResponse("QUERY HAS BEEN RAISED",safe=False)


# PENNDING QUERY

def SHOW_ALL_PENDING_QUERY(request):
    
    if request.method=='GET':
        query_element=quires.objects.filter(STATUS="PENDING").values()        
        print(list(query_element))      
        return JsonResponse(list(query_element),safe=False)

# REJECT QUERY    
    
def REJECT_STUDENT_QUERY(request):
    data=json.loads(request.body)
    USER_NAME=data['USER_NAME']    
    quires.objects.filter(USER_NAME=USER_NAME).update(STATUS="REQUEST REJECTED")
    students.objects.filter(USER_NAME=USER_NAME).update(STATUS="REQUEST REJECTED")
    return JsonResponse("rejected",safe=False)

# APPROVE QUERY

def APPROVE_STUDENT_QUERY(request):
    data=json.loads(request.body)
    USER_NAME=data['USER_NAME']
    quires.objects.filter(USER_NAME=USER_NAME).update(STATUS="REQUEST APPROVED")
    students.objects.filter(USER_NAME=USER_NAME).update(STATUS="REQUEST APPROVED")
    return JsonResponse("approved",safe=False)

# UPDATE STUDENT QUERY

def UPDATE_STUDENT_QUERY(request):
    data=json.loads(request.body)
    USER_NAME=data['USER_NAME']
    father_name=data['father_name']
    email=data['email']
    branch=data['branch']
    phone_no=data['phone_no']
    num=students.objects.filter(USER_NAME=USER_NAME,STATUS='REQUEST APPROVED').exists()
    if(num):
        students.objects.filter(USER_NAME=USER_NAME,STATUS='REQUEST APPROVED').update(father_name=father_name,email=email,branch=branch,phone_no=phone_no)
        print("updated successfully")
        return JsonResponse("success updation",safe=False)
    else:
        return JsonResponse("YOUR REQUEST HAS NOT BEEN APPROVED YET ",safe=False)

