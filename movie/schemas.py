from pydantic import BaseModel, Field
from typing import Optional
from fastapi import Query

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3, max_length=15)
    overview: str = Field(min_length=15, max_length=100)
    year: int = Field(le=2022)
    rating: float = Field(default=1, ge=1, le=10)
    category: str = Field(default='Acción', min_length=5, max_length=15)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Mi película",
                    "overview": "Descripción de la película",
                    "year": 2022,
                    "rating": 9.8,
                    "category": "Acción"
                }
            ]
        }
    }


class MovieCreate(BaseModel):
    title: str = Field(min_length=3, max_length=15)
    overview: str = Field(min_length=15, max_length=100)
    year: int = Field(le=2022)
    rating: float = Field(default=1, ge=1, le=10)
    category: str = Field(default='Acción', min_length=5, max_length=15)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Mi película",
                    "overview": "Descripción de la película",
                    "year": 2022,
                    "rating": 9.8,
                    "category": "Acción"
                }
            ]
        }
    }
    
class MovieSearchParams(BaseModel):
    category: Optional[str] = None
    year: Optional[int] = None
    rating: Optional[float] = None