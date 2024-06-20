from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from project.Config import Config

db = SQLAlchemy()

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def init_app(app):
    db.init_app(app)


def get_session():
    return Session()