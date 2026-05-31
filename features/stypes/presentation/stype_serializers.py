from rest_framework import serializers

class CreateSerializer(serializers.Serializer):
    stype_name = serializers.CharField(required=True)

class UpdateSerializer(serializers.Serializer):
    stype_id = serializers.CharField(required=True)
    stype_name = serializers.CharField(required=True)

class GetByColumnSerializer(serializers.Serializer):
    stype_id = serializers.CharField(required=True)
    stype_name = serializers.CharField(required=True)

class StypeResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    stype_id = serializers.CharField(required=True)
    stype_name = serializers.CharField(required=True)