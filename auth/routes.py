from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.security import HTTPBearer
from jose.jwt import encode, decode
from .schemas import UserAuth

router = APIRouter(
    tags=['auth'],
)


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")


def create_token(data: dict):
    token = encode(claims=data, key='my_secret_key', algorithm='HS256')
    return token


def validate_token(token: str) -> dict:
    data: dict = decode(token, key='my_secret_key', algorithms=['HS256'])
    return data


@router.post('/login')
def login(user: UserAuth):
    if user.email == 'admin@gmail.com' and user.password == 'admin':
        token: str = create_token(user.model_dump())
        return token
    return 'No user found'
