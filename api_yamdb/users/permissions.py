from rest_framework import permissions


class IsAuthorAdminOrModeratorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'POST':
            return bool(request.user and request.user.is_authenticated)

        return bool(
            request.user and (
                request.user == obj.author or
                request.user.role in ['admin', 'moderator'] or
                request.user.is_staff)
        )


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return (
                request.user.role in ['admin'] or
                request.user.is_staff
            )

        return False


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role in ['admin'] or
            request.user.is_staff
        )
