from rest_framework.permissions import BasePermission

class CheckRolePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'client'

class CreateHotelPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'owner'