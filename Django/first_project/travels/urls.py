from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name='index'),
    path("destinations/<int:id>/", views.destinations, name='destinations'),
    path("comments/<int:id>/", views.comments, name='comments'),
]