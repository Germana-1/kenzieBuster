from rest_framework import permissions


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_employee


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user == obj
            or request.user.is_authenticated
            and request.user.is_employee
        )
