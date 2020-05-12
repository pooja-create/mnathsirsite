from django.urls import path
from development import views

urlpatterns = [
     path('',views.alldev,name='alldev'),
    path('<int:development_id>/',views.detail,name='details'),
    
]