from pydantic import BaseModel, BeforeValidator, Field
from datetime import datetime
from typing import Annotated, Optional

PyObjectId = Annotated[str, BeforeValidator(str)]
class Users(BaseModel):
    uid: Optional[PyObjectId] = Field(alias="_id", default=None)
    ty_pe: str | None
    full_name: str | None
    username: str | None
    email: str | None
    password: str| None
    submitted_by: datetime | None
    updated_by: datetime | None