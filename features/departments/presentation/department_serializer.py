from rest_framework import serializers
from features.rooms.presentation.room_serializers import RoomResponseSerializer

class DepartmentCreateSerailizer(serializers.Serializer):
    department_name = serializers.CharField(required=True)
    room_id = serializers.CharField(required=True, allow_null=True, allow_blank=True)

class DepartmentUpdateSerailizer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    department_id = serializers.CharField(required=True)
    department_name = serializers.CharField(required=True)
    room_id = serializers.CharField(required=True)

class GetByColumnSerailizer(serializers.Serializer):
    id = serializers.IntegerField(required=True, allow_null=True)
    department_id = serializers.CharField(required=True, allow_null=True)
    department_name = serializers.CharField(required=True, allow_null=True)
    room_id = serializers.CharField(required=True, allow_null=True)

class DepartmentResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True, allow_null=True)
    department_id = serializers.CharField(required=True, allow_null=True)
    department_name = serializers.CharField(required=True, allow_null=True)
    room_id = serializers.CharField(required=True, allow_null=True)
    room = RoomResponseSerializer(required=True, allow_null=True)
    message = serializers.CharField(required=True, allow_null=True)

