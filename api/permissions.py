from rest_framework.permissions import BasePermission


class IsReferee(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.referee


class IsOptions(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'OPTIONS'