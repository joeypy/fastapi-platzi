from fastapi import APIRouter, Path, Query, Depends
from sqlalchemy.orm import Session
from typing import List

from auth.routes import JWTBearer
from config.database import get_db
from .models import Movie as MovieModel
from .schemas import Movie

router = APIRouter(
    # prefix='movies',
    tags=['movies']
)

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': 2009,
        'rating': 7.8,
        'category': 'Acción'
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': 2009,
        'rating': 7.8,
        'category': 'Aventura'
    },
    {
        'id': 3,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': 2009,
        'rating': 7.8,
        'category': 'Acción'
    }
]


# dependencies=[Depends(JWTBearer())]
@router.get('/movies', response_model=List[Movie], status_code=200)
async def get_movies(db: Session = Depends(get_db)):
    # return movies
    return db.query(MovieModel).all()


@router.get('/movies/', status_code=200)
async def get_movie_by_category(category: str = Query(min_length=5, max_length=15)):
    return [movie for movie in movies if movie['category'].casefold() == category.casefold()]


@router.get('/movies/{id}', status_code=200)
async def get_movie_by_id(id: int = Path(ge=1, le=2000)):
    for movie in movies:
        if movie['id'] == id:
            return movie
    return 'No movie was found!'


@router.post('/movies', status_code=201)
async def create_movie(body: Movie):
    movies.append(dict(body))
    return 'Movie was created!'


@router.delete('/movies/{id}', status_code=200)
async def delete_movie_by_id(id: int = Path(ge=1, le=2000)):
    for i in range(len(movies)):
        if movies[i].get('id') == id:
            movies.pop(i)
            return {'message': 'Movie deleted'}
        return {'message': 'Not movie fount'}
