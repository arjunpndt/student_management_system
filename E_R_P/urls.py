
from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^E_R_P_students/',include('E_R_P_students.urls')),
   url(r'^teacher/',include('teacher.urls')),
   url(r'^quires/',include('quires.urls')),
]
