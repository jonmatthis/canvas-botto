
--- NOTES ---

learning about developer keys:

https://canvas.instructure.com/doc/api/file.developer_keys.html


... 

Had a chat, got my bearings, but the guides were busted. 

--- GUIDE --- 

## Getting a access key

https://canvas.instructure.com/profile/settings#registered_web_services


Purpose: CanvasBot testing
Expiration date and time: 2 options:
  - leave blank and delete them when you run out
  - set to end of semester, re-up if you need it. 

Click generate:
- as with all generated keys, copy it out NOW and put it somewhere safe (even if that's just a text file on your computer right this second). NOT somewhere public. 
- you'll get an email verifying that this happened

my test token: 7~x4UBKVZHXvxFENwK9F9KzaRvwNtQKQYxmuHchrVyc6TGcyetExrmVHmzLa3kV4ht

curl -H "Authorization: Bearer 7~x4UBKVZHXvxFENwK9F9KzaRvwNtQKQYxmuHchrVyc6TGcyetExrmVHmzLa3kV4ht" "https://canvas.instructure.com/api/v1/courses"

get it into .env, baby. This will be stored behind the scenes and not at all exposed in discord. Admin/developer only.


--- NOTES --- 

new search: I guess I still need a `long-lived` developer key.

realizing I didn't have an admin account. 

AHA-- research fruitful: 
- one CANNOT do any of this through a free instructure account. 
- We need to either 
  - run our own instance (oh!)
  - or we need to get the flow down 

- running our own instance sounds cooler and more fun, but it's not the primary use case. I'll get more into the institution-level. 

...

OR maybe we don't need anything but the personal access token, as long as it's the professor's. let's find out. 



--- NOTES --- 

Okay, revisiting the access token we created in the user's account: 

https://canvas.instructure.com/doc/api/file.oauth.html#using-access-tokens

```sh
curl -H "Authorization: Bearer 7~x4UBKVZHXvxFENwK9F9KzaRvwNtQKQYxmuHchrVyc6TGcyetExrmVHmzLa3kV4ht" "https://canvas.instructure.com/api/v1/courses"
```

```json
[{
    "id":10844022,
    "name":"Your Guided Course Template",
    "account_id":102391,"uuid":"8bluSFJwcVli756wHAL4gGOcCxB1BWvNRGsAdaKf","start_at":null,
    "grading_standard_id":null,
    "is_public":false,
    "created_at":"2024-12-13T01:52:59Z","course_code":"NA-COURSE-TEMPLATE",
    "default_view":"modules",
    "root_account_id":10,
    "enrollment_term_id":1,
    "license":"private",
    "grade_passback_setting":null,
    "end_at":null,
    "public_syllabus":false,
    "public_syllabus_to_auth":false,
    "storage_quota_mb":262,
    "is_public_to_auth_users":false,
    "homeroom_course":false,
    "course_color":null,
    "friendly_name":null,
    "apply_assignment_group_weights":false,
    "calendar":{
        "ics":"https://canvas.instructure.com/feeds/calendars/course_8bluSFJwcVli756wHAL4gGOcCxB1BWvNRGsAdaKf.ics"
        },
    "time_zone":"America/Denver",
    "blueprint":false,
    "template":false,
    "sis_course_id":null,
    "integration_id":null,
    "enrollments":[
        {"type":"teacher",
        "role":"TeacherEnrollment",
        "role_id":994,
        "user_id":114664109,
        "enrollment_state":"active","limit_privileges_to_course_section":false
        }
    ],
    "hide_final_grades":false,"workflow_state":"unpublished","restrict_enrollments_to_course_dates":false
}]
```

SUCCESS. We've "gotten" a list of course blobs associated with this token. 

If we can read and write, we're fuckin' gucci, baby.

Let's boogie. 

--- GUIDE --- 

## Testing your access token

Pop open a terminal and paste this, replacing the `<ACCESS_TOKEN>` bit with your actual token

```sh
curl -H "Authorization: Bearer <ACCESS_TOKEN>" "https://canvas.instructure.com/api/v1/courses"
```

This'll try to grab a list of the courses you're connected to, and in what capacity. 

```json
[{
    "id":10844022,
    "name":"Your Guided Course Template",
    "account_id":102391,"uuid":"8bluSFJwcVli756wHAL4gGOcCxB1BWvNRGsAdaKf","start_at":null,
    "grading_standard_id":null,
    "is_public":false,
    "created_at":"2024-12-13T01:52:59Z","course_code":"NA-COURSE-TEMPLATE",
    "default_view":"modules",
    "root_account_id":10,
    "enrollment_term_id":1,
    "license":"private",
    "grade_passback_setting":null,
    "end_at":null,
    "public_syllabus":false,
    "public_syllabus_to_auth":false,
    "storage_quota_mb":262,
    "is_public_to_auth_users":false,
    "homeroom_course":false,
    "course_color":null,
    "friendly_name":null,
    "apply_assignment_group_weights":false,
    "calendar":{
        "ics":"https://canvas.instructure.com/feeds/calendars/course_8bluSFJwcVli756wHAL4gGOcCxB1BWvNRGsAdaKf.ics"
        },
    "time_zone":"America/Denver",
    "blueprint":false,
    "template":false,
    "sis_course_id":null,
    "integration_id":null,
    "enrollments":[
        {"type":"teacher",
        "role":"TeacherEnrollment",
        "role_id":994,
        "user_id":114664109,
        "enrollment_state":"active","limit_privileges_to_course_section":false
        }
    ],
    "hide_final_grades":false,"workflow_state":"unpublished","restrict_enrollments_to_course_dates":false
}]
```


--- NOTES --- 

progress banked. now to explore with some questions in mind:

Questsss
- What all do we have in this endpoint that will help us achieve our goals?
  - explicate goals
  - find components involved
  - test them
- Are there any substantive limitations on the long-lived user access tokens?


Let's just test some readwrite capacities first...

... wait, I'm gonna search for something...

--- 

OOH SHIT, new excursion, discovered:

`pip install canvasapi`
https://github.com/ucfopen/canvasapi (MIT license)

Still actively up-to-date, it seems to claim. 


bless 'em, they've got some docs
https://canvasapi.readthedocs.io/en/stable/troubleshooting.html#access-token
- seems this one WANTS access tokens, which is perfect. 

---


New questions charted:
- Once I have IDs, are professors free to reorganize them within the course without a catastrophe?


and next practical question is: 
do I have access to other endpoints?
- ew, seems like maybe no.


Looking for submissions features for canvas-api... 
may need to roll my own

https://canvas.instructure.com/doc/api/submissions.html


Eyyyy maybe not

https://github.com/ucfopen/canvasapi/blob/develop/canvasapi/submission.py



OOH, alternate route to the canvas course ID: 
`https://canvas.instructure.com/courses/10844022` -- just go to the course page, it's this, lol. 

niccccce

if we're lucky, canvas's standard permissions structure for professors and students will handle the whole thing. 



Looking like you need to be a student to submit an assignment. 


--- 

building a test student-- throwing this at jon

1. go enroll as a student here:
https://canvas.instructure.com/enroll/HB8XA4

2. then go here
https://canvas.instructure.com/profile/settings#registered_web_services
- Approved Integreations > [+ New Access Token]

gimme. 


--- 

okay, jon's testing with. 

figuring out how to post assignments publicly. 


new things we should access:
- assignments
  - /create
- submissions
  - /submit - by default, this discord URL link
- courses
  - can't create a course, so we need them to set it up at the server level
  - /link_course: connects discord server ID with canvas course. 
- /link_user_account: takes their access_token
  - we store their access token with their discord ID for use with their stuff
  - all other commands must error out if this hasn't happened yet. 
- /create_assignment: performs the assignment generation, but also binds it to the current discord channel ID. 

bindings for this transport layer: 
- discord-canvas-ids: canvas_student_id, canvas_user_access_token, discord_id
- course-server: canvas_course_id, discord_server_id, canvas_user_access_token (professor)
- assignment: canvas_assignment_id, discord_channel_id;
  - only available to `professor` role, requires professor to have bound their access_token
- submission: will use the discord channel ID to create a new submission for the given assignment 


Opinionation: lockstep with 1 server, 1 course. No exceptions. 
Opinionation: assignments must be created in channels, and submissions must come from threads inside those channels. 
Opinionation: we will not enable auto-grading in any way. students can either be given full credit for submissions, or no credit. 

No Opinion: folder structures within canvas -- we only ever use the ID. 


you have to... UNHIDE the ASSIGNMENTS tab??
https://canvas.instructure.com/courses/10844022/details#tab-navigation
- didn't help tho. still getting forbidden. 


OKAY, no, all we needed to do was specify what types of submissions are valid. 

--- 

We are now officially in a position where we can handle all of the details, and can even write simple user guides. 



