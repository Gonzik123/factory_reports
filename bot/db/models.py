from sqlalchemy import Column, Integer, Text, DateTime, String, Boolean, Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import JSONB

import enum
from datetime import datetime
from zoneinfo import ZoneInfo

Base = declarative_base()

def now_msk():
    return datetime.now(ZoneInfo("Europe/Moscow"))

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
    created_at = Column(DateTime, default=now_msk())
    update_at = Column(DateTime, default=now_msk(), onupdate=now_msk())