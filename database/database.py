from sqlalchemy import create_engine
from .schema import Base

engine = create_engine("sqlite:///database/database.db", echo=True)

Base.metadata.create_all(engine)

