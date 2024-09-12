from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('job', views.JobViewset, basename='job')
router.register('company', views.CompanyViewset, basename='company')
router.register('user', views.CustomUserViewset, basename='user')

urlpatterns = [
    path('api/', include(router.urls))
]