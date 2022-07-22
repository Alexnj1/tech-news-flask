from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key = True)
  title = Column(String(100), nullable = False)
  post_url = Column(String(100), nullable = False)
  # references the user table, id column
  user_id = Column(Integer, ForeignKey('users.id'))
  created_at = Column(DateTime, default = datetime.now)
  updated_at = Column(DateTime, default = datetime.now, onupdate=datetime.now)

  # counts the votes on the given post from the Vote table
  # SELECT COUNT(votes.id) AS vote_count FROM votes WHERE votes.post_id = <1 for example>;
  vote_count = column_property(select([func.count(Vote.id)]).where(Vote.post_id == id))

  # the point of these is that when the data is queried, you can see the subsets of user and comment data that belong to each Post
  user = relationship('User')
  comments = relationship('Comment', cascade='all,delete')
  votes = relationship('Vote', cascade='all,delete')