# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://canvas.instructure.com/"
# Canvas API key
API_KEY = ""


# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

print(canvas)

user = canvas.get_current_user()

print(user)

print(user)

print(user.get_user_logins())
for login in user.get_user_logins():
    print(login)

print(user.get_courses())
for course in user.get_courses():
    print(course)
    print(course.id)

# forces selection of first course
course_id = user.get_courses()[0].id

course = canvas.get_course(course_id)

print(course)

users = course.get_users()


print(users)
for user in users:
    print(user)

assignments = course.get_assignments()
print(assignments)
for assignment in assignments:
    print(assignment)

# creating assignments for a course-- WORKS
#   notes: 
#       - always creates fresh with new ID
#       only do these actions once when meaningful.
#       - assignments spawn hidden

# new_assignment = course.create_assignment({
#     'name': 'fort. night.',
#     'published': True,
#     'submission_types': ['online_text_entry','online_url'],
#     'allowed_attempts': -1,
#     'points_possible': 1,
# })



# # more complex
# new_assignment = course.create_assignment({
#     'name': 'Assignment 3',
#     'submission_types': ['online_upload'],
#     'allowed_extensions': ['docx', 'doc', 'pdf'],
#     'notify_of_update': True,
#     'points_possible': 100,
#     'due_at': datetime(2018, 12, 31, 11, 59),
#     'description': 'Please upload your homework as a Word document or PDF.',
#     'published': True
# })


# print(new_assignment)


API_KEY_STUDENT = ""
canvas_student = Canvas(API_URL, API_KEY_STUDENT)

course_student = canvas_student.get_course(course_id)

assignment_student = course_student.get_assignment(51671046)

print(assignment_student)

# current issue: I have to be a student in the course for this to work. 
# assignment_student.submit({
#     "submission_type": "online_text_entry",
#     "body": "I am submitting this assignment."
# })







# new_assignment.delete()




