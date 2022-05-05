import json

from contextlib import contextmanager
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
engine = create_engine('sqlite:///sqlite3.db')


@contextmanager
def session():
    connection = engine.connect()
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))
    try:
        yield db_session
    except Exception as e:
        print(e)
    finally:
        db_session.remove()
        connection.close()


class KenoRaw(Base):
    __tablename__ = 'keno_raw'
    id = Column(Integer, primary_key=True, autoincrement=True)
    keno_label = Column(String(50))  # KN353828
    balls = Column(String(300))

    def get_row(self):
        balls = json.loads(self.balls)
        return balls


Base.metadata.create_all(engine)
