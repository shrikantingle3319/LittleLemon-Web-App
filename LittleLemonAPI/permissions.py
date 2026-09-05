from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    """
    Allows access only to users in the Manager group.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.is_staff
                or request.user.groups.filter(
                    name="Manager"
                ).exists()
            )
        )


class IsManagerOrReadOnly(BasePermission):
    """
    Anyone can read.
    Only managers can create/update/delete.
    """

    def has_permission(self, request, view):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.is_staff
                or request.user.groups.filter(
                    name="Manager"
                ).exists()
            )
        )