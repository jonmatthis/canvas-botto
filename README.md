# Canvas Course Info Script

This script allows you to retrieve information about the courses you are teaching on Canvas using a Python script.

## Setup

1. **Obtain Your Canvas API Key:**
   - **Log in to Canvas:**
   - **Navigate to your Account Settings:**
     - Click on your profile picture or account icon in the top left corner.
     - Select `Settings` from the dropdown menu.
   - **Generate a New Access Token:**
     - Scroll down to the `Approved Integrations` section.
     - Click on `+ New Access Token`.
     - Fill in the purpose of the token, such as "Canvas Course Info Script".
     - **Expiration Date (Optional):** You can set an expiration date for security reasons.
     - Click `Generate Token`.
   - **Copy the Token:**
     - Copy the generated token immediately and store it securely. You won't be able to view it again.

2. **Environment Variables:**
   - Create a `.env` file in the same directory as the script and add your Canvas API key :
     ```plaintext
     CANVAS_API_KEY=<Your_Canvas_API_Key>
     ```

## Installation

1. **Python and pip:**
   - Ensure you have Python 3.x and `pip` installed on your system.

2. **Install Required Packages:**
   - Run the following command to install the necessary libraries:
     ```bash
     pip install canvasapi python-dotenv
     ```

## Usage

- Run the script using the following command:
  ```bash
  python canvas_course_info.py
  ```
- The script will print a list of your courses with their IDs and names.

## Expected Results

- The output will display the course IDs and names for all courses associated with your Canvas account.
  
```plaintext
Course ID: 123456, Course Name: Introduction to Programming
Course ID: 789012, Course Name: Advanced Data Science
```
```

### Additional Notes:

- Ensure the `.env` file is in the same directory as the script and contains the correct API key.
- The script requires the `canvasapi` and `python-dotenv` packages. Make sure they are installed using pip.
- The script assumes you have a valid Canvas access token with the necessary permissions to access course information.

Feel free to modify the script and README as needed to fit your specific requirements or preferences!