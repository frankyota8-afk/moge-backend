from rest_framework import serializers
from features.roles.models import Role

class RoleResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    role_id = serializers.CharField()
    role_name = serializers.CharField()
