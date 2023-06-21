from rest_framework.permissions import BasePermission


class CustomUserBasedPermission(BasePermission):
    def has_permission(self, request, view):
        # Check the user_type of the authenticated user
        user_type = request.user.user_type

        # Endpoints only Admin user can access
        allowed_admin_endpoints = ['add-song']

        # Define the permissions based on user_type
        if user_type == 'admin' and request.resolver_match.view_name in allowed_admin_endpoints:
            return True
        elif user_type == 'enduser' and request.resolver_match.view_name not in allowed_admin_endpoints:
            return True

        return False
