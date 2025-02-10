from canvasapi import Canvas
import os
from dotenv import load_dotenv

from canvas_botto.canvas_models import CanvasCourse

# Load environment variables from a .env file
load_dotenv()

# Canvas API URL and Key
API_URL = "https://canvas.instructure.com/"
API_KEY = os.getenv('CANVAS_API_KEY')
CANVAS_COURSE_CODE = os.getenv('CANVAS_COURSE_CODE')
if API_KEY is None:
    raise ValueError("Please set the CANVAS_API_KEY environment variable.")
if CANVAS_COURSE_CODE is None:
    raise ValueError("Please set the CANVAS_COURSE_CODE environment variable.")
    
# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

def get_course_by_code(course_code: str):
    user = canvas.get_current_user()
    courses = user.get_courses()

    for course in courses:
        if course.course_code == course_code:
            return course

    raise ValueError(f"Course with code {course_code} not found.")
if __name__ == "__main__":
    course = get_course_by_code(course_code=CANVAS_COURSE_CODE)
    users = list(course.get_users())
    for user in users:
        print(user)