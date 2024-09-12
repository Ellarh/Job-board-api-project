from .models import Company, CustomUser, Job
from .serializers import JobSerializer, CompanySerializer, CustomUserSerializer
from rest_framework import viewsets
from .permissions import IsEmployer, IsJobSeeker
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache import cache


class JobViewset(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    @method_decorator(cache_page(settings.CACHE.TTL))
    def list(self, request, *args, **kwargs):
        return super(JobViewset, self).list(request, *args, **kwargs)

    def perform_create(self, serializer):
        cache.clear()
        return super().perform_create(serializer)

    def perform_update(self, serializer):
        cache.clear()
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        cache.clear()
        return super().perform_destroy(instance)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsEmployer]
        else:
            permission_classes = [IsAuthenticated, IsJobSeeker]
        return [permission() for permission in permission_classes]


class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsEmployer]


class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]














