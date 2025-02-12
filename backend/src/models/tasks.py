import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID


Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    is_completed = Column(Boolean, nullable=False, default=False)