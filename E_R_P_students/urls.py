from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^student_login/$',views.STUDENT_LOGIN_FUN,name="STUDENT_LOGIN_FUN"),
    url(r'^students_view/$',views.STUDENT_DATA,name="STUDENT_DATA"),
    url(r'^change_password/$',views.CHANGE_STUDENT_PASSWORD,name="CHANGE_STUDENT_PASSWORD"),  
    url(r'^profile_update/$',views.UPDATE_STUDENT_PROFILE,name="UPDATE_STUDENT_PROFILE"),  
   
]