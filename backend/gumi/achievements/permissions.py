from rest_framework.permissions import BasePermission, AllowAny, IsAuthenticated

class AcheivementPermission(BasePermission):
    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, ]

        return super(UsersViewSet, self).get_permissions()