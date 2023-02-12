from fastapi import FastAPI
from .database import get_db

app = FastAPI()

# db: Session = Depends(get_db)

@app.get('/')
def test():
    return {'message': 'Success!'}