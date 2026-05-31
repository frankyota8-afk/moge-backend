from rest_framework import serializers
from features.roles.presentation.serializer.response_serializer import RoleResponseSerializer
from features.departments.presentation.department_serializer import DepartmentResponseSerializer
from features.ranks.presentation.rank_serializers import RankResponseSerializer
from features.stypes.presentation.stype_serializers import StypeResponseSerializer

class StaffCreateSerializer(serializers.Serializer):

    staff_name = serializers.CharField(required=True)
    staff_email = serializers.CharField(required=True)
    staff_address = serializers.CharField(required=True)
    staff_ph_number = serializers.CharField(required=True)
    staff_gender = serializers.CharField(required=True)

    department_id = serializers.IntegerField(required=True, allow_null=True)
    role_id = serializers.IntegerField(required=True, allow_null=True)
    rank_id = serializers.IntegerField(required=True, allow_null=True)
    stype_id = serializers.IntegerField(required=True, allow_null=True)

class StaffUpdateSerializer(serializers.Serializer):

    id = serializers.IntegerField(required=True)
    staff_id = serializers.CharField(required=True)
    staff_name = serializers.CharField(required=True)
    staff_email = serializers.CharField(required=True)
    staff_address = serializers.CharField(required=True)
    staff_ph_number = serializers.CharField(required=True)
    staff_gender = serializers.CharField(required=True)

    department_id = serializers.IntegerField(required=True, allow_null=True)
    role_id = serializers.IntegerField(required=True, allow_null=True)
    rank_id = serializers.IntegerField(required=True, allow_null=True)
    stype_id = serializers.IntegerField(required=True, allow_null=True)

class StaffGetByColumnSerializer(serializers.Serializer):

    staff_id = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    staff_name = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    staff_email = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    staff_address = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    staff_ph_number = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    staff_gender = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    department_id = serializers.IntegerField(required=False, allow_null=True)
    role_id = serializers.IntegerField(required=False, allow_null=True)
    rank_id = serializers.IntegerField(required=False, allow_null=True)
    stype_id = serializers.IntegerField(required=False, allow_null=True)
  
class StaffResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    staff_id = serializers.CharField()
    staff_name = serializers.CharField()
    staff_email = serializers.CharField()
    staff_address = serializers.CharField()
    staff_ph_number = serializers.CharField()
    staff_gender = serializers.CharField()

    department_id = serializers.IntegerField()
    role_id = serializers.IntegerField()
    rank_id = serializers.IntegerField()
    stype_id = serializers.IntegerField()

    department = DepartmentResponseSerializer()
    role = RoleResponseSerializer()
    rank = RankResponseSerializer()
    stype = StypeResponseSerializer()
  
