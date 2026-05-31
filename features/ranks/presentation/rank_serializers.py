from rest_framework import serializers

class CreateSerializer(serializers.Serializer):
    rank_name = serializers.CharField(required=True)

class UpdateSerializer(serializers.Serializer):
    rank_id = serializers.CharField(required=True)
    rank_name = serializers.CharField(required=True)

class GetByColumnSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    rank_id = serializers.CharField(required=False)
    rank_name = serializers.CharField(required=False)

class RankResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    rank_id = serializers.CharField(required=True)
    rank_name = serializers.CharField(required=True)