from rest_framework import serializers

from users.models import User, Role, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    role = RoleSerializer()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'role', 'bio', 'gender', 'location', 'birth_date', 'phone']
