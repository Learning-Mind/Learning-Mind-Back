from typing import Generic, TypeVar
from pydantic import BaseModel

PayloadT = TypeVar("PayloadT")

class APIErrorScheme(BaseModel):
    code: int
    message: str
    clientMessage: str | None = None

class APIResponseSchema(BaseModel, Generic[PayloadT]):
    success: bool
    payload: PayloadT | None = None
    error: APIErrorScheme | None = None