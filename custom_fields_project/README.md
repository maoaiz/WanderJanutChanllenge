
# Custom fields project

## Summary
This project will allow managers to generate dynamic forms for the different teams on the ground. The project is a web platform that stores the forms and the data uploaded with those forms.

## Scope
We will have different sections to different user types:

* **Auth**: The service is available to all our internal users using or SSO (single sing on) service.
* **Admin Forms**: A managers section for creating dynamic forms.
* **Forms**: A section to see the available forms and register new answers.

## Modeling
Our data model is described with the next figure:

![Database model](imgs/db.png "Database model")

We have a User resource allowed to create Forms and Questions, a FieldType resource to define the type of input that should be used for each Question and an Answer resource to store all anwers provided every time that a form is used.

A new form is available once all questions are defined and the form is finished. The form is available while it is marked as published.

Users (the team) can use the published forms to record new answers at any time.

## Interface Flow
### Managers site
1. The manager logs in.
2. The manager can see a list of all their created forms.
3. The manager can create a new form using the "New form" button.
4. The manager enters a form name.
5. The manager can create N questions for the form using the "New question" button.
6. The manager enters a question name and a type of field.
    Available types:
    * Short text: input
    * Long text: textarea
    * File (image or document): file
    * etc.
7. The manager must finish the edition of the form and should mark it as published.
8. The manager can update or remove forms and questions.

### Team site
1. The user logs in.
2. The user see a list of published (available) forms.
3. The user selects a form to register a new answer.
4. The user fills all questions and register the answer using the button "Save answer"
5. The user sees a success or error message saving the answers
6. The user is not able to update or remove answers.

## API
The backend team will implement the next endpoints: 

### Manager:
| Endpoint | Description |
|---|---|
| GET /forms | Retrieve the list of all own forms |
| POST /forms | Creates a new form |
| GET /forms/id | Retrieve the details of a form |
| PUT /forms/id | Updates an existing form |
| DELETE /forms/id | Deletes the selected form |
| GET /forms/id/questions | Retrieves the list of the questions of a form |
| POST /forms/id/questions | Creates a new question for the selected form |
| PUT /forms/id/questions/id | Updates a selected question in the selected form |
| DELETE /forms/id/questions/id | Deletes the selected question in the form |
| GET /field-types | Retrieves the available field types |

### Users:
| Endpoint | Description |
|---|---|
| GET /available-forms | Retrieve the list of the available forms |
| GET /available-forms/id | Retrieve the questions of the selected form |
| POST /available-forms/id/anwers | Creates all the answers filled in the form |



Mauricio Aizaga

**Lead Product engineer**