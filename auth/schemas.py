from pydantic import BaseModel, Field


class UserAuth(BaseModel):
    email: str = Field(min_length=3, max_length=30)
    password: str = Field(min_length=3, max_length=30)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": 'joeypc.py@gmail.com',
                    "password": "hola",
                }
            ]
        }
    }
