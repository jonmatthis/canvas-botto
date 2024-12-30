# CanvasBot Setup Guide (Professor/Admin)

This guide helps you quickly set up CanvasBot so students and you can access course data via a chat interface (e.g. Slack). After setup, it’s mostly “set and forget.”

## Prerequisites
- Canvas admin access (to create Developer Keys).
- A Canvas course ID (from the course URL).
- A communication platform token (e.g. Slack Bot Token).

## Steps

1. **Create a Developer Key in Canvas**
   - In Canvas, go to Admin > Developer Keys > +Developer Key > API Key.
   - Name it and save.
   - Toggle the new key to “On.”

2. **Obtain a Canvas Access Token**
   - In Canvas: Profile > Settings > +New Access Token.
   - Copy the token immediately.

3. **Get Your Course ID**
   - Visit your course’s Canvas page and note the numeric ID in the URL.

4. **Configure CanvasBot**
   - Provide these values to the CanvasBot configuration:
     - Canvas domain (e.g. https://institution.instructure.com)
     - Your access token
     - The course ID
     - The chat platform token (e.g. Slack Bot Token)

5. **Deploy CanvasBot**
   - Follow the provided deployment instructions.
   - Ensure all environment variables are set correctly.

6. **Integration with Chat Platform**
   - For Slack, install the Slack App and add the Bot Token to CanvasBot.
   - Now users can type commands (e.g. “/canvasbot assignments”) to see Canvas info.

## Maintenance
- Replace the access token if it expires.
- Update the course ID if the course changes.
- Otherwise, no regular upkeep required.

Once set up, CanvasBot runs quietly in the background, ready to help students and you access Canvas course data via your preferred chat tool.