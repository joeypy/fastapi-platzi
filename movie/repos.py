from sqlalchemy import and_
from sqlalchemy.orm import Session
from .models import Movie as MovieModel
from .schemas import MovieCreate, MovieUpdate


class MovieRepo:

    @staticmethod   
    def get_all_movies(db: Session) -> MovieModel:
        return db.query(MovieModel).all()

    @staticmethod
    def get_movies_by_parameters(db: Session, **kwargs) -> MovieModel:
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
    def update_movie(db: Session, movie_id: int, movie_data: MovieUpdate) -> MovieModel:
        movie_to_update = MovieRepo.get_movie_by_id(db, movie_id)
        print(movie_to_update)
        for key, value in movie_data.model_dump().items():
            if value is not None:
                setattr(movie_to_update, key, value)
        db.commit()
        db.refresh(movie_to_update)
        return movie_to_update
    
    @staticmethod
    def delete_movie(db: Session, movie_id: int) -> MovieModel:
        try:
            movie_deleted = db.query(MovieModel).filter(MovieModel.id == movie_id).delete()
            db.commit()
            return bool(movie_deleted)
        except:
            return False

    