from canvasapi import Canvas
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Canvas API URL and Key
API_URL = "https://canvas.instructure.com/"
API_KEY = os.getenv('CANVAS_API_KEY')
if API_KEY is None:
    raise ValueError("Please set the CANVAS_API_KEY environment variable.")

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)


def get_course_info():
    user = canvas.get_current_user()
    courses = user.get_courses()

    course_info = []
    for course in courses:
        info = {
            'id': course.id,
            'name': course.name
        }
        course_info.append(info)

    return course_info


if __name__ == "__main__":
    courses = get_course_info()
    for course in courses:
        print(f"Course ID: {course['id']}, Course Name: {course['name']}")