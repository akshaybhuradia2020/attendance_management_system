from pydantic import BaseModel, BeforeValidator, Field
from datetime import datetime
from typing import Annotated, Optional

PyObjectId = Annotated[str, BeforeValidator(str)]
class Students(BaseModel):
    sid: Optional[PyObjectId] = Field(alias="_id", default=None)
    full_name: str | None
    department_id: str | None
    clss: str | None
    submitted_by: datetime | None
    updated_by: datetime | None