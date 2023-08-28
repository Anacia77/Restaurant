from rest_framework import permissions

class IsAdminOrManager(permissions.BasePermission):
    def permission(self, request, view):
        return request.user.is_superuser or request.user.groups.filter(name='Manager').exists()