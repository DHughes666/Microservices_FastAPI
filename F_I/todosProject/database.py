from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

engine = create_engine(
    SQALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autoflush=False, autocommit=False,
    bind=engine)

Base = declarative_base()