first thought

`/commands`

- `/submit` - student-facing command - submits a full copy of the conversation, as well as the LAST full message + attachments specifically into a canvas submission folder organized in the same way as the server
  - or, if not mirroring the structure, according to some key retrieved from the parent channel. 
  - this process involves matching the student's ID in the database, as well as the id of the thing in question. 
  - this design depends on which is easier inside the ecosystem. 
    - there's support for more complex queries, so, we can see. 

- `/make_assignment` - educator-facing command - , a new assignment id, and does the same on the target canvas environment
  - deploys a link to the discord channel itself
  - marks down in the channel the ID of the canvas assignment

tagging things with emojis can help for submissiony-connectivity

We, as an organiziation, do not respect or participate in the concept of grading. 

---

Canvas structure:
- thinking *flat* and *auxiliary* (nothing depends on canvas)
- 

Server Deploying:
- some opinionated basic server structure that covers good bases
  - an AI prompt made to help generate these deploy jsons later, given things like, syllabus, etc. 
- defaults:
    - how-to-bot channel
    - advanced tech


Discord functionalities:
- BUTTONS
  - /submit
  - 

Walkthrough: 
- based on the default demo

Discord Server Structure:
- Deconstruct Jon's current servers into what Types Of Things
  - assignment channels
  - exploration channels(?)
  - intro chats: at least 5 couplets. 

- discord-focused assignment types:
  - minimum-length-chats - open ended paritciation - automatic submission based on length
  - explicit-submission-chats - submit this entire thing when you're good
  - targeted artifact chats - somehow capture a targeted attachment

Cron jobs:
- checking status of server stuff
- nudging students if they have something incomplete this week

Message components:
- control panel at the top of a chat
- bot message panel -- button to bring up the ephemeral control panel for the user to interact with. 
- not the same as embeds maybe?
- modals - 



--- 

as far as next semester goes, skelly-bot doesn't need to be rebuilt
- I do obviously need to integrate canvas stuff, though. 


that said...
- db checkpoints dumped into the server every day at midnight
  - PROGRESS CAPTURE, prevents rollbacks, fully transparent, interoperable with local runs


Most of the work this past semester was the Skellybot Analysis server
- data re-scraping was a main concern
- near the end, mongo querying...
  - json-dump


