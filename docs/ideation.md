

`/commands`


- `/submit` - student-facing command - submits a full copy of the conversation, as well as the LAST full message + attachments specifically into a canvas submission folder organized in the same way as the server
  - or, if not mirroring the structure, according to some key retrieved from the parent channel. 
  - this process involves matching the student's ID in the database, as well as the id of the thing in question. 
  - this design depends on which is easier inside the ecosystem. 
    - there's support for more complex queries, so, we can see. 

- `/make_assignment` - educator-facing command - creates a new channel, a new assignment id, and does the same on the target canvas environment




