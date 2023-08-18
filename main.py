from fastapi import FastAPI
from movie.routes import router as router_movies
from auth.routes import router as router_auth
from config.database import SessionLocal, engine, Base
from movie.models import Movie

app = FastAPI(
    title='Platzi course',
    version='0.0.1'
)

Base.metadata.create_all(bind=engine)

v1_prefix = "/api/v1"
app.include_router(router_auth, prefix=v1_prefix)
app.include_router(router_movies, prefix=v1_prefix)


@app.get('/', tags=['home'])
async def message():
    return 'Hello World!'


