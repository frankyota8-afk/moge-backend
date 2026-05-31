from rest_framework import serializers

class GetByColumnSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    role_id = serializers.CharField(required=False)
    role_name = serializers.CharField(required=False)