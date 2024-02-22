from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    signup_date = Column(DateTime, server_default=func.now())
    rank_points = Column(Integer, default=0)
    last_online = Column(DateTime, onupdate=func.now())
    username = Column(String(50), unique=True)
    email = Column(String, unique=True)
    password_hash = Column(String)
    avatar = Column(String)
    posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")
    friends_list = relationship("FriendsList", back_populates="owner",cascade="all, delete-orphan" )

user_preference = Table(
    "user_preference",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("users.id")),
    Column("name", String(100), nullable=False),
    Column("value", String(100))
)

class FriendsList(Base):
    __tablename__ = "friends_list"
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="friends_list")
    friends = relationship("User")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    body = Column(String(40000), nullable=False)
    date_posted = Column(DateTime, server_default=func.now())
    kudos = Column(Integer, default=1)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    author = relationship("User", back_populates="posts")

class GameData(Base):
    __tablename__ = "game_data"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    winner_id = Column(Integer, ForeignKey("users.id"))
    players = relationship("Player", back_populates="game", cascade="all, delete-orphan")

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))
    game_id = Column(Integer, ForeignKey("game_data.id"))
    user = relationship("User")
    character = relationship("Character")
    game = relationship("GameData", back_populates="players")


class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    play_data = relationship("Player", back_populates="character")
