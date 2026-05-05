# ===============================================
# Data: 27/04/2026
# Autor: Pedro Teixeira Gontijo
# ===============================================

import hashlib
import secrets
from django.db import transaction
from typing import Optional, Tuple
from .models import ApiClient, ApiToken


class ApiTokenService:
    TOKEN_BYTES = 64
    PREFIX_SIZE = 12

    @classmethod
    def gerar_token_raw(cls) -> str:
        return secrets.token_urlsafe(cls.TOKEN_BYTES)

    @staticmethod
    def gerar_hash(token_raw: str) -> str:
        return hashlib.sha256(token_raw.encode("utf-8")).hexdigest()

    @classmethod
    @transaction.atomic
    def criar_token(cls, cliente: ApiClient) -> Tuple[ApiToken, str]:
        token_raw = cls.gerar_token_raw()
        token_hash = cls.gerar_hash(token_raw)
        prefix = token_raw[: cls.PREFIX_SIZE]

        api_token = ApiToken.objects.create(
            cliente=cliente,
            ativo=True,
            prefix=prefix,
            token_hash=token_hash,
        )

        return api_token, token_raw

    @classmethod
    def validar_token(cls, token_raw: str) -> Optional[ApiToken]:
        token_hash = cls.gerar_hash(token_raw)

        api_token = (
            ApiToken.objects
            .select_related("cliente")
            .filter(
                token_hash=token_hash,
                ativo=True,
                cliente__ativo=True,
            )
            .first()
        )

        return api_token