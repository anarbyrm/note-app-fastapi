from fastapi import FastAPI
from pydantic import BaseModel
from .database import get_db, engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# db: Session = Depends(get_db)

@app.get('/')
def test():
    return {'message': 'Success!'}