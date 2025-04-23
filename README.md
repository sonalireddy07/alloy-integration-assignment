# alloy-integration-assignment

Introduction:
  This project is a take-home assignment for Alloy’s Solutions Architect role. The goal was to build a Python script that integrates with the Alloy sandbox API to submit applicant identity information and return a decision based on the evaluation outcome.

My Approach:
  1. Collecting applicant details

  2. Submitting the details to the Alloy API

  3. Processing the API response and presenting an appropriate message

  For collecting input, I considered two approaches: hardcoding versus accepting user input via the console. While hardcoding would’ve been faster, I opted for console input to make the script more dynamic and usable. This choice meant adding validation logic to guide the user and ensure required fields were properly formatted.

  A key question I kept in mind while designing the input flow was: How should this behave for both the user and the system? For instance, the Date of Birth must follow the ISO-8601 format (YYYY-MM-DD). If the user enters an invalid format, the script should prompt them to try again until it’s valid. This ensures clean data before sending it to Alloy.

  All applicant details were stored in a dictionary matching the expected field structure and then passed into the Alloy API using a POST request. The API response was parsed, and depending on the outcome field, a corresponding message was displayed.

Challenges and Learnings
