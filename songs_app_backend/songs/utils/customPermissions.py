from rest_framework.permissions import BasePermission


class CustomUserBasedPermission(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            print('My User is not authenticated.')
            return False

        # Check the user_type of the authenticated user
        user_type = request.user.user_type
        print('user type is: ', user_type)
        print(request)
        print('*****')
        allowed_admin_endpoints = ['add-song']

        # Define the permissions based on user_type
        if user_type == 'admin':
            if request.resolver_match.view_name in allowed_admin_endpoints:
                print('admin is access add song endpoint')
                return True
            # Admin users have access to all endpoints
            print('admin is access some other endpoint')
            return False
        elif user_type == 'enduser':
            if request.resolver_match.view_name not in allowed_admin_endpoints:
                print('enduser is accessing his endpoints')
                return True
            print('enduser is accessing his endpoints')
            return False
        print('invalid usertype')
        return False
