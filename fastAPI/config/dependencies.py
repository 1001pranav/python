from config.db import SessionLocal
from contextlib import contextmanager

@contextmanager
def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

db_context = contextmanager(get_db)