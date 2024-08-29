from rest_framework import serializers

from users.models import User, Role, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    role = serializers.SlugRelatedField(queryset=Role.objects.all(), slug_field='name')

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'role', 'bio', 'gender', 'location', 'birth_date', 'phone']