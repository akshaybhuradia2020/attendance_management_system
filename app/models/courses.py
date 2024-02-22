from pydantic import BaseModel, BeforeValidator, Field
from datetime import datetime
from typing import Annotated, Optional

PyObjectId = Annotated[str, BeforeValidator(str)]
class Courses(BaseModel):
    cid: Optional[PyObjectId] = Field(alias="_id", default=None)
    course_name: str | None
    department_id: str | None
    clss: str | None
    semester: int | None
    lecture_hours: float | None
    submitted_by: datetime | None
    updated_by: datetime | None