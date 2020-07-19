from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^teacher_login/$',views.TEACHER_LOGIN_FUN,name="TEACHER_LOGIN_FUN"),
    url(r'^students/$',views.ALL_ACTIVE_STUDENT,name="ALL_ACTIVE_STUDENT"),
    url(r'^insert/$',views.INSERT_NEW_STUDENT,name="INSERT_NEW_STUDENT"),
    url(r'^delete/$',views.STUDENT_INACTIVE_FUN,name="STUDENT_INACTIVE_FUN"),
    url(r'^update/$',views.UPDATE_SUDENT_PROFILE,name="UPDATE_SUDENT_PROFILE"),    
]
