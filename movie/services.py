from sqlalchemy.orm import Session

from .repos import MovieRepo
from .schemas import MovieCreate, Movie


class MovieService:

    @staticmethod
    def get_all_movies(db: Session):
        return MovieRepo.get_all_movies(db)
    
    @staticmethod
    def get_movies_by_parameters(db: Session, **kwargs):
        return MovieRepo.get_movies_by_parameters(db, **kwargs)
    
    @staticmethod
    def get_movie_by_id(db: Session, movie_id: int):
        return MovieRepo.get_movie_by_id(db, movie_id)

    @staticmethod
    def create_movie(db: Session, movie: MovieCreate):
        return MovieRepo.create_movie(db, movie)
    
    @staticmethod
    def delete_movie(db: Session, movie_id: int):
        return MovieRepo.delete_movie(db, movie_id)
