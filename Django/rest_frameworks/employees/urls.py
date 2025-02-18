from . import  views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('',views.Employee,basename='employee')

urlpatterns = [
    # path("",views.AllEmployee.as_view(),name="all_employees"),
    # path("<int:id>/",views.Employee.as_view(),name="employee"),
    path('',include(router.urls)),
]
