from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from jobs import views
urlpatterns=[
   path('',views.home,name='home'),
   path('<int:job_id>/',views.detail,name='details'),
   
]
