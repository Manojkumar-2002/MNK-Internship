from . import  views
from django.urls import path

urlpatterns = [
    path("",views.AllEmployee.as_view(),name="all_employees"),
    path("<int:id>/",views.Employee.as_view(),name="employee"),
]
