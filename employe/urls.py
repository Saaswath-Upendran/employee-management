from django.urls import path
from .views import *

app_name = "employe"

urlpatterns = [
    path("",HomePage.as_view(),name="home"),
    path('createuser/',register_user,name="create"),
    path('employe/',EmployeList.as_view(),name='list'),
    path('employe_detail/<int:pk>',EmployeDetail.as_view(),name='details'),
    path('employe_update/<int:pk>',EmployeUpdate.as_view(),name='update'),
    path('employe_delete/<int:pk>',EmployeDelete.as_view(),name='delete'),
]