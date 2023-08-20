from sqlalchemy import and_
from sqlalchemy.orm import Session
from .models import Movie as MovieModel
from .schemas import MovieCreate


class MovieRepo:

    @staticmethod   
    def get_all_movies(db: Session) -> MovieModel:
        return db.query(MovieModel).all()

    @staticmethod
    def get_movies_by_parameters(db: Session, **kwargs) -> MovieModel:
        # filters = {key: value for key, value in kwargs.items() if value is not None}
        conditions = [getattr(MovieModel, key).ilike(f"%{value}%") for key, value in kwargs.items() if value is not None]
        return db.query(MovieModel).filter(*conditions).all()
    
    @staticmethod
    def get_movie_by_id(db: Session, movie_id: int) -> MovieModel:
        return db.query(MovieModel).get(movie_id)

    @staticmethod
    def create_movie(db: Session, movie: MovieCreate) -> MovieModel:
        new_movie = MovieModel(**movie.model_dump())
        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)
        return new_movie
    
    @staticmethod
    def delete_movie(db: Session, movie_id: int) -> MovieModel:
        try:
            movie_deleted = db.query(MovieModel).filter(MovieModel.id == movie_id).delete()
            db.commit()
            return bool(movie_deleted)
        except:
            return False

    