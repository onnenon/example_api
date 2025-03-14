from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, scoped_session, sessionmaker


class Base(DeclarativeBase):
    pass


engine = create_engine("sqlite:///test.db")

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base.query = db_session.query_property()


def init_db():
    import py_api.models  # noqa: F401

    Base.metadata.create_all(bind=engine)
