from django.conf.urls import url
from . import views



urlpatterns = [
    # url(r'^$',views.index,name="index"),
    url(r'^ans_query/$',views.SHOW_ALL_PENDING_QUERY,name="SHOW_ALL_PENDING_QUERY"),
    url(r'^rejection/$',views.REJECT_STUDENT_QUERY,name="REJECT_STUDENT_QUERY"),
    url(r'^approval/$',views.APPROVE_STUDENT_QUERY,name="APPROVE_STUDENT_QUERY"),
    url(r'^query_update/$',views.UPDATE_STUDENT_QUERY,name="UPDATE_STUDENT_QUERY"),
    url(r'^query_raisal/$',views.RAISE_STUDENT_QUERY,name="RAISE_STUDENT_QUERY"),
     
]