from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.models import User, UserProfile, Role
from users.serializers import UserSerializer, UserProfileSerializer, RoleSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter the queryset to only show the profile of the currently authenticated user
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Associate the profile with the currently authenticated user
        serializer.save(user=self.request.user)


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]
