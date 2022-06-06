from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in ['admin']
            or request.user.is_staff
        )


class IsAdminNoModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated
            and request.user.role in ['admin']
        )


class IsAuthorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            and request.user.is_anonymous
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'DELETE']:
            return (
                obj.author == request.user
                or request.user.is_staff
                or request.user.get_role in ['admin']
            )
        return True


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return (
                request.user.role in ['admin']
            )

        return False


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsAuthorOrAdminOrModeratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            and request.user.is_anonymous
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method in ['POST']:
            return (
                request.user.is_authenticated
            )

        if request.method in ['PATCH', 'DELETE']:
            return (
                obj.author == request.user
                or request.user.is_staff
                or request.user.role in ['admin', 'moderator']
            )
        return True
