# Alloy's Integration Assignment

## Introduction:
This project is a take-home assignment for Alloy’s Solutions Architect role. The goal was to build a Python script that integrates with the Alloy sandbox API to submit applicant identity information and return a decision based on the evaluation outcome.

## My Approach:
  1. Collecting applicant details

  2. Submitting the details to the Alloy API

  3. Processing the API response and presenting an appropriate message

  For collecting input, I considered two approaches: hardcoding versus accepting user input via the console. While hardcoding would’ve been faster, I opted for console input to make the script more dynamic and usable. This choice meant adding validation logic to guide the user and ensure required fields were properly formatted.

  A key question I kept in mind while designing the input flow was: How should this behave for both the user and the system? For instance, the Date of Birth must follow the ISO-8601 format (YYYY-MM-DD). If the user enters an invalid format, the script should prompt them to try again until it’s valid. This ensures clean data before sending it to Alloy.

  All applicant details were stored in a dictionary matching the expected field structure and then passed into the Alloy API using a POST request. The API response was parsed, and depending on the outcome field, a corresponding message was displayed.

## Challenges and Learnings
One minor challenge came from how I initially structured the request payload. I had mistakenly wrapped the data inside a data key, and although the API responded with 200 OK, the response didn’t include the expected summary field. This was confusing at first, since a 200 usually indicates success.

After looking through Alloy’s API documentation more carefully, I learned that a 200 response doesn’t guarantee that an evaluation was performed — it can also mean that required inputs were missing. I traced the issue to how I was submitting the first name field, which was being passed at the wrong level in the payload. Once I adjusted the structure to match Alloy’s expectations, the request succeeded and returned a proper evaluation outcome.

This experience gave me a deeper understanding of Alloy’s evaluation model and emphasized the importance of aligning precisely with an API’s data schema. To prevent similar issues, I added a loop in the script to ensure that required fields like the first name are provided before submitting the request.

## Improvements
  1. Add handling for unexpected responses, such as a 201 Created status with no outcome in the response body.

  2. Expand validation coverage for user input — ensuring all non-null and critical fields meet format expectations before submission.

  3. Add logging throughout the request flow to provide transparency on what the script is doing at each step and make debugging easier in the future.
