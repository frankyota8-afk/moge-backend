from rest_framework.views import APIView, Response, Request
from .helpers import getDepartmentCount, getDocumentCount, getStaffCount


class DashboardView(APIView):
    
    def get(self, request: Request)->Response:
        return Response({
            "summary" : {
                "count" : {
                    "staffs" : getStaffCount(),
                    "documents" : getDocumentCount(),
                    "departments" : getDepartmentCount(),
                }
            }
        })