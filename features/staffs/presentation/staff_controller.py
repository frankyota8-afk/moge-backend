from rest_framework.views import APIView, Request, Response
from features.staffs.presentation.staff_serializers import StaffCreateSerializer, StaffUpdateSerializer, StaffResponseSerializer, StaffGetByColumnSerializer
from features.staffs.application.contracts.request_contracts import StaffCreateContract, StaffUpdateContract, StaffDeleteContract, StaffGetByIdContract, StaffGetByColumnContract
from features.staffs.application.services.staff_service import StaffService

class StaffController(APIView):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def toApiResponse(self,data)->Response:
        return Response(data=data)

    def post(self, request: Request)->Response:
        serializer = StaffCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        contract = StaffCreateContract(**serializer.validated_data)

        staff,message = StaffService.createStaff(contract)

        return self.toApiResponse({"staff" : StaffResponseSerializer(staff).data, "message" : message})
    
    def get(self, request: Request)->Response:
        
        staffs = StaffService.allStaffs()

        res = StaffResponseSerializer(staffs, many=True)

        return self.toApiResponse({"staffs" : res.data})

    def put(self, request : Request, id:int)->Response:

        serializer = StaffUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contract = StaffUpdateContract(**serializer.validated_data)
        
        staff,message = StaffService.updateStaff(contract)

        res= StaffResponseSerializer(staff)

        return self.toApiResponse({"staff" : res.data, "message" : message})
    
    def delete(self, request:Request, id:int)->Response:
        contract = StaffDeleteContract(id=id)

        message = StaffService.deleteStaff(contract)

        return self.toApiResponse({"message" : message})
    
class GetStaffByIdView(APIView):
    def get(self, request:Request, id:int)->Response:

        contract = StaffGetByIdContract(id=id)

        staff = StaffService.getStaffsById(contract)

        return Response({
            "staff" : StaffResponseSerializer(staff).data
        })
    
class GetStaffByColumnView(APIView):

    def get(self, request:Request)->Response:

        serializer = StaffGetByColumnSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        contract = StaffGetByColumnContract(**serializer.validated_data)

        staffs = StaffService.getStaffsByColumn(contract)

        return Response({
            "staffs" : StaffResponseSerializer(staffs, many=True).data
        })
    




        



        




