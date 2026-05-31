# common/security/middleware/jwt_middleware.py
from django.http import JsonResponse
from common.security.utils.jwt_utils import verify_jwt

class JWTMiddleware:
    """
    Extracts JWT and attaches payload to request
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth = request.headers.get("Authorization")

        if auth and auth.startswith("Bearer "):
            token = auth.split(" ")[1]
            try:
                payload = verify_jwt(token)
                request.jwt_payload = payload
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=401)

        return self.get_response(request)
