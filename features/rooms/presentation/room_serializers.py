from rest_framework import serializers

class CreateSerializer(serializers.Serializer):
    room_no = serializers.CharField(required=True)
    room_name = serializers.CharField(required=True)
    building_id = serializers.IntegerField(required=True, allow_null=True)

class UpdateSerializer(serializers.Serializer):
    room_id = serializers.CharField(required=True)
    room_no = serializers.CharField(required=True)
    room_name = serializers.CharField(required=True)
    building_id = serializers.IntegerField(required=True, allow_null=True)

class GetByColumnSerializer(serializers.Serializer):
    room_id = serializers.CharField(required=True, allow_null=True)
    room_no = serializers.CharField(required=True, allow_null=True)
    room_name = serializers.CharField(required=True, allow_null=True)
    building_id = serializers.IntegerField(required=True, allow_null=True)

class BuildingResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    building_id = serializers.CharField(required=True)
    building_name = serializers.CharField(required=True)

class RoomResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    room_id = serializers.CharField(required=True)
    room_no = serializers.CharField(required=True)
    room_name = serializers.CharField(required=True)
    building_id = serializers.IntegerField(required=True, allow_null=True)
    building = BuildingResponseSerializer()