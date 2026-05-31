from rest_framework import serializers

class UpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    role_id = serializers.CharField(required=True)
    role_name = serializers.CharField(required=True)