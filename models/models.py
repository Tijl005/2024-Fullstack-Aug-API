from pydantic import BaseModel

class tour(BaseModel):
    tourId: int
    firstName: str
    lastName: str
    email: str
