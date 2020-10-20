from rest_framework.permissions import BasePermission, AllowAny, IsAuthenticated

class Permission(BasePermission):
    def get_permissions(self):

        if self.request.method == 'GET':
            self.permission_classes = [AllowAny,]
        else:
            self.permission_classes = [IsAuthenticated,]
        
        return super(UsersViewSet, self).get_permissions()