from pydantic import BaseModel
from typing import List

class Operation(BaseModel):
    """
    Pydantic model for an RPN operation.
    Accepts a list of strings representing the RPN expression.
    """
    operation: List[str]  # List of operations or numbers in RPN format
