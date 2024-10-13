
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('course', views.CourseModelView, basename='course')

urlpatterns = [
  
   
    path('api-auth/', include('rest_framework.urls')),
     path('', include(router.urls)),
]
