from pydantic import BaseModel, BeforeValidator, Field
from datetime import datetime
from typing import Annotated,  Optional


PyObjectId = Annotated[str, BeforeValidator(str)]
class Departments(BaseModel):
    did: Optional[PyObjectId] = Field(alias="_id", default=None)
    department_name: str | None
    submitted_by: datetime | None
    updated_by: datetime | None