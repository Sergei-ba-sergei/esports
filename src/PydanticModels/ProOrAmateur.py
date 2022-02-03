from typing import Optional
from pydantic import BaseModel

# The simplest model anyone has ever seen
class Name(BaseModel):
    name: str
