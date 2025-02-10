from pydantic import BaseModel
from typing import List, Optional


class Calendar(BaseModel):
    ics: Optional[str]


class Enrollment(BaseModel):
    type: str
    role: str
    role_id: int
    user_id: int
    enrollment_state: str
    limit_privileges_to_course_section: bool


class CanvasCourse(BaseModel):
    id: int
    name: str
    account_id: int
    uuid: str
    start_at: Optional[str]
    grading_standard_id: Optional[int]
    is_public: bool
    created_at: str
    course_code: str
    default_view: str
    root_account_id: int
    enrollment_term_id: int
    license: Optional[str]
    grade_passback_setting: Optional[str]
    end_at: Optional[str]
    public_syllabus: bool
    public_syllabus_to_auth: bool
    storage_quota_mb: int
    is_public_to_auth_users: bool
    homeroom_course: bool
    course_color: Optional[str]
    friendly_name: Optional[str]
    apply_assignment_group_weights: bool
    calendar: Optional[Calendar]
    time_zone: str
    blueprint: bool
    template: bool
    sis_course_id: Optional[str]
    integration_id: Optional[str]
    enrollments: List[Enrollment]
    hide_final_grades: bool
    workflow_state: str
    restrict_enrollments_to_course_dates: bool
