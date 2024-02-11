
from ctypes import Array
from datetime import datetime
from turtle import back
from typing import List
from sqlalchemy import ARRAY, UUID, Column, DateTime, ForeignKey, Integer, String, Uuid, func
from .database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship


 
class Post(Base):
    __tablename__ = "posts"
    id: Mapped[Uuid] = mapped_column(UUID(as_uuid=True), primary_key=True)
    body: Mapped[str] = mapped_column(String(40000))
    tags = Column(ARRAY(String))
    date_posted: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    kudos: Mapped[int] = mapped_column(Integer, default=1)
    author_id: Mapped[Uuid] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship(back_populates="user")

class MatchData(Base):
    __tablename__ = "match_data"
    id: Mapped[Uuid] = mapped_column(Uuid, primary_key=True)
    date: Mapped[datetime] = mapped_column(DateTime)
    winner_id: Mapped[Uuid] = mapped_column(ForeignKey("user.id"))
    players: Mapped["MatchPlayers"] = relationship('User', uselist=True, backref="users" secondary=MatchPlayers)

class User(Base):
    __tablename__ = "users"
    id: Mapped[Uuid] = mapped_column(Uuid(as_uuid=True), primary_key=True)
    signup_date: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    last_online: Mapped[DateTime] = mapped_column(DateTime, onupdate=datetime.now())
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[String] = mapped_column(String, unique=True)
    hashword: Mapped[str] = mapped_column(String)
    posts: Mapped[List["Post"]] = relationship(back_populates="user")

class MatchPlayers(Base):
    __tablename__ = "match_players"
    user_id: Mapped[Uuid] = mapped_column(UUID(as_uuid=True), ForeignKey('user.id'))
    match_id: Mapped[Uuid] = mapped_column(UUID(as_uuid=True), ForeignKey('match_data.id'))