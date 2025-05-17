from sqlalchemy import Column, Integer, Text, DateTime, String, Boolean, Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import JSONB

import enum
from datetime import datetime
import pytz


Base = declarative_base()

def now_msk():
    return datetime.now(pytz.timezone('Europe/Moscow'))

class UserRole(enum.Enum):
    inspector = "inspector"
    admin = "admin"


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(Enum(UserRole, name='user_role', native_enum=True, create_type=False))
    banned = Column(Boolean, default=False)
    ban_reason = Column (Text)
    created_at = Column(DateTime(timezone=True), default=now_msk)
    updated_at = Column(DateTime(timezone=True), default=now_msk, onupdate=now_msk)