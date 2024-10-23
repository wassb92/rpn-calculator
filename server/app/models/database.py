from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Calculation(Base):
    """
    Represents a calculation entry in the database.
    Stores the RPN expression and its result.
    """
    __tablename__ = "calculations"
    
    id = Column(Integer, primary_key=True, index=True)  # Unique ID for each calculation
    expression = Column(String, index=True)  # The RPN expression
    result = Column(String, index=True)  # The result of the calculation
