# ===============================================
# Data: 27/04/2026
# Autor: Pedro Teixeira Gontijo
# ===============================================

from rest_framework.permissions import BasePermission
from .services import ApiTokenService


class ValidApiToken(BasePermission):
    message = "Autenticação não válida."

    def has_permission(self, request, view):
        auth_header = request.headers.get("Authorization", "")

        if not auth_header.startswith("Bearer "):
            return False

        token_raw = auth_header.split(" ", 1)[1].strip()
        api_token = ApiTokenService.validar_token(token_raw)

        if not api_token:
            return False

        request.api_token = api_token
        request.api_client = api_token.cliente

        return True