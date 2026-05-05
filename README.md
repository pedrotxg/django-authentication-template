# Django Bearer Token Authentication — Template
> Este repositório é um molde (template) mínimo para autenticação via Bearer Token em projetos Django. O objetivo é servir como ponto de partida — implementar geração/validação de tokens e regras de permissão conforme sua necessidade.

## Funcionalidade
- Molde para autenticação por token Bearer em Django.
- Estrutura de exemplo localizada em `Authentication/` (modelos, serviços e permissões).

## Estrutura relevante
- [Authentication/models.py](Authentication/models.py): modelos relacionados ao usuário/credenciais (se aplicável).
- [Authentication/services.py](Authentication/services.py): funções de geração e validação de token.
- [Authentication/permissions.py](Authentication/permissions.py): classes de permissão que usam o token para autorizar requisições.

> Ajuste os arquivos acima para implementar a lógica de criação e verificação do token.

## Requisitos
- Python 3.8+ (ajuste conforme necessário)
- Dependências listadas em `requirements.txt` — instale com pip.


## Instalação rápida

1. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\Activate     # Windows PowerShell
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Execute migrações e crie um superusuário (opcional):

```bash
python manage.py migrate
python manage.py createsuperuser
```

## Como funciona (visão geral)
- O servidor deve expor uma rota (ex.: `/api/token/`) que gera um token para um usuário autenticado (login).
- O cliente envia o token nas requisições autenticadas usando o cabeçalho `Authorization: Bearer <token>`.
- No lado do servidor, a validação do token pode ser feita em middleware, classes de autenticação ou nas permissões das views.

Exemplo de cabeçalho HTTP:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```


## Exemplo de uso com curl

1. Obtenha o token (endpoint de exemplo; adapte ao seu):

```bash
curl -X POST https://localhost:8000/api/token/ -d '{"username":"meu_usuario","password":"senha"}' -H "Content-Type: application/json"
# resposta: {"token": "<seu_token_aqui>"}
```

2. Acesse um endpoint protegido com o token:

```bash
curl -H "Authorization: Bearer <seu_token_aqui>" https://localhost:8000/api/protected-endpoint/
```

## Dicas de implementação
- Para geração/validação de tokens, considere usar JWT (`PyJWT`) ou tokens assinados conforme suas necessidades.
- Centralize a lógica de verificação em `Authentication/services.py` e reutilize nas `permissions.py` ou em uma `Authentication` class personalizada.
- Proteja endpoints sensíveis usando classes de permissão que checam o token e o escopo/claims.

## Testes
Execute os testes do app:

```bash
python manage.py test
```

## Contribuições
Este é um template — fique à vontade para abrir issues ou PRs com melhorias, exemplos e integrações (ex.: refresh tokens, expiração, blacklist).