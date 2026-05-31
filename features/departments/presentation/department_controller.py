from rest_framework.views import APIView, Request, Response
from features.departments.presentation.department_serializer import GetByColumnSerailizer, DepartmentResponseSerializer, DepartmentCreateSerailizer, DepartmentUpdateSerailizer
from features.departments.application.contracts.create_contract import DepartmentCreateContract
from features.departments.application.contracts.update_contract import DepartmentUpdateContract
from features.departments.application.contracts.delete_contract import DepartmentDeleteContract
from features.departments.application.contracts.getByColumn_contract import GetByColumnContract
from features.departments.infrastructure.department_repository import DepartmentRepository
from features.departments.application.department_services import DepartmentServices
from features.departments.application.contracts.getById_contract import GetByIdContract
from rest_framework import status, generics

class DepartmentController(APIView):

    def __init__(self):
        self.service = DepartmentServices(DepartmentRepository())

    def get(self, request : Request)->Response:
        if request.query_params:
            serializer = GetByColumnSerailizer(data=request.query_params)
            serializer.is_valid(raise_exception=True)
            contract = DepartmentCreateContract(**serializer.validated_data)
            res = self.service.getDepartmentbyColumn(contract=contract)
        else:
            res = self.service.allDepartments()

        return Response({
            "departments" : DepartmentResponseSerializer(res, many=True).data
        })
    
    def post(self, request : Request)->Response:
        serializer = DepartmentCreateSerailizer(data=request.data)
        serializer.is_valid(raise_exception=True)

        contract = DepartmentCreateContract(**serializer.validated_data)
        res = self.service.creatDepartment(contract)

        return Response({
            "department" : DepartmentResponseSerializer(res).data,
            "message" : "Created successfully!",
        })
    
    def put(self, request: Request, id:int)->Response:
        serializer = DepartmentUpdateSerailizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contract = DepartmentUpdateContract(**serializer.validated_data)
        res, message = self.service.updateDepartment(contract)

        return Response({
            "department" : DepartmentResponseSerializer(res).data,
            "message" : message,
        })
    
    def delete(self, request:Request, id:int)->Response:
        contract = DepartmentDeleteContract(id=id)

        message = self.service.deleteDepartment(contract)

        return Response({
            "message" : message,
        })
    
class DepartmentListView(generics.ListAPIView):
    serializer_class = DepartmentResponseSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = DepartmentServices(DepartmentRepository())

    def get_queryset(self , request : Request):
        
        serializer = GetByColumnSerailizer(request.query_params)
        serializer.is_valid(raise_exception=True)

        contract = GetByColumnContract(**serializer.validated_data)

        return self.service.getDepartmentbyColumn(contract)
    
class GetDepartmentByIdView(APIView):

    def __init__(self):
        self.service = DepartmentServices(DepartmentRepository())

    def get(self, requst:Request, id:int)->Response:

        contract = GetByIdContract(id=id)
        department = self.service.getDepartmentbyId(contract)

        return Response({
            "department" : DepartmentResponseSerializer(department).data
        })
        
