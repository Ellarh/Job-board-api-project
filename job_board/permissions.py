from rest_framework.permissions import BasePermission


class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'E'


class IsJobSeeker(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'J':
            return request.method in ['GET', 'HEAD', 'OPTIONS']
        return False
