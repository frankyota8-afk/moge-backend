from rest_framework.response import Response
from features.staffs.domain.staff_entity import StaffEntity
from dataclasses import asdict


def contractToEntity(contract)->StaffEntity:
    contract = asdict(contract)

    return StaffEntity(**{
        k:v for k,v in contract.items()
    })

def toApiResponse(data = "", message=""):
    return Response({
        "data" : data,
        "message" : message
    })
    
