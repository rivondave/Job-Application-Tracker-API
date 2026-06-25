from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
    DateTime
)

from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

from app.core.database import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(
        String,
        nullable=False
    )

    job_title = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        default="Applied"
    )

    notes = Column(String)

    date_applied = Column(Date)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    owner = relationship(
    "User",
    back_populates="applications"
)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )