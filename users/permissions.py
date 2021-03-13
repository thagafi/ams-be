from rest_framework import permissions

from .serializers import UserSerializer


class ViewPermissions(permissions.BasePermission):

    # def has_permission(self, request, view):
    #     data = UserSerializer(request.user).data

    #     view_access = any(p['codename'] == 'view_' + view.permission_object for p in data['role']['permissions'])
    #     edit_access = any(p['codename'] == 'change_' + view.permission_object for p in data['role']['permissions'])

    #     if request.method == 'GET':
    #         return view_access or edit_access

    #     return edit_access

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
