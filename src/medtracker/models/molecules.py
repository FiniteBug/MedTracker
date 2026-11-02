from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from medtracker.db.base import Base

class Molecules(Base):
    __tablename__ = "molecules"

    # Key
    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    formula: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[str] = mapped_column(nullable=False, unique=False)