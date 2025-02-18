from . import  views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_nested.routers import NestedDefaultRouter


router = DefaultRouter()
router.register('blogs',views.Blog,basename='blogs')
router.register('comments', views.Comment, basename='comments') 

# comment_router = NestedDefaultRouter(router, 'blogs', lookup='blog')
# comment_router.register('comments', views.Comment, basename='comments')

urlpatterns = [
    path('',include(router.urls)),
    # path('',include(comment_router.urls))
]
