from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("news/", views.about, name='news'),
    path("contact/", views.about, name='contact'),
    path("destinations/<int:id>/", views.destinations, name='destinations'),
    path("comments/<int:id>/", views.comments, name='comments'),
]