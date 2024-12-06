from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    birthday = Column(Date)
    email = Column(String, unique=True, index=True)
    mobile_number = Column(String)
    level = Column(String)
    role = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Organization_categories(Base):
    __tablename__ = "organization_categories"

    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Organization_units(Base):
    __tablename__ = "organization_units"

    id = Column(Integer, primary_key=True, index=True)
    unit_name = Column(String)
    category_id = Column(Integer)
    parent_unit_id = Column(Integer)
    leader_id = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class User_organization_units(Base):
    __tablename__ = "user_organization_units"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    unit_id = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())