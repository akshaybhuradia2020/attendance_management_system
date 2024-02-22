from pydantic import BaseModel, BeforeValidator, Field
from datetime import datetime
from typing import Annotated, Optional

PyObjectId = Annotated[str, BeforeValidator(str)]
class Attendance_Log(BaseModel):
    mid: Optional[PyObjectId] = Field(alias="_id", default=None)
    student_id: str | None
    course_id: str | None
    present: bool | None
    submitted_by: datetime | None
    updated_by: datetime | None