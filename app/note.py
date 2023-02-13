from fastapi import FastAPI, Depends
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from .database import get_db, engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

