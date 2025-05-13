from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)  # ✅ Uzunluk eklendi
    hashed_password = Column(String(100))  # ✅ Uzunluk eklendi

class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)  # ✅ Uzunluk eklendi
    owner_id = Column(Integer, ForeignKey("users.id"))

class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)  # ✅ Uzunluk eklendi
    user_id = Column(Integer, ForeignKey("users.id"))

class Adoption(Base):
    __tablename__ = "adoptions"
    id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, ForeignKey("pets.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
