from rest_framework import serializers

class CreateSerializer(serializers.Serializer):
    role_name = serializers.CharField(required=True)
