from sqlalchemy import Column, String, Date,  DateTime
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base


class Note(Base):
    __tablename__ = 'notes'
    
    title = Column(String, nullable=False, unique=True)
    content = Column(String, nullable=False)
    till_date = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
    