from fastapi import APIRouter, HTTPException, Path, Query, Depends
from sqlalchemy import and_
from sqlalchemy.orm import Session
from typing import List

from auth.routes import JWTBearer
from config.database import get_db
from .schemas import Movie, MovieCreate, MovieSearchParams
from .services import MovieService

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
    return MovieService.get_all_movies(db)


@router.get('/movies_by', response_model=List[Movie], status_code=200)
async def get_movies_by(
        category: str = Query(None, description="Category to filter"),
        year: int = Query(None, description="Year to filter"),
        rating: float = Query(None, description="Rating to filter"), 
        db: Session = Depends(get_db)
    ):
    search_params = MovieSearchParams(category=category, year=year, rating=rating) 
    if search_params:
        return MovieService.get_movies_by_parameters(db, **search_params.model_dump())
    return []
        
    

@router.get('/movies/{id}', status_code=200)
async def get_movie_by_id(id: int = Path(ge=1, le=2000), db: Session = Depends(get_db)):
    return MovieService.get_movie_by_id(db, id)


@router.post('/movies', status_code=201)
async def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    new_movie = MovieService.create_movie(db, movie)
    return {'data': new_movie, 'message': 'Movie was created!'}



@router.delete('/movies/{id}', status_code=200)
async def delete_movie_by_id(id: int = Path(ge=1, le=2000), db: Session = Depends(get_db)):
    try:
        movie_deleted = MovieService.delete_movie(db, id)
        if movie_deleted:
            return {'msg': 'Movie deleted successfully', 'status': True}
        return {'msg': 'Movie not found', 'status': False}
    except Exception as e:
        return {'msg': f'Error: {e}', 'status': False}
