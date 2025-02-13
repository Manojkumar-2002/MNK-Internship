from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="basic"),
    path('education/<int:id>',views.education,name="education"),
    path('bank/<int:id>',views.bank,name="bank"),
    path('prev_emp/<int:id>',views.prev_emp,name="prev_emp"),
    path('details/<int:id>',views.home,name="home"),
    path('employee/<int:id>/pdf/', views.generate_employee_pdf, name='employee_pdf'),
]
