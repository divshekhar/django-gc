# Django Google Calendar

Google calendar OAuth2 integration using Django REST API.

## Steps

Here are the steps you can follow to create a Google Calendar API in the Google Cloud Console:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/) and sign in with your Google account.

2. In the dashboard, click on the "Select a Project" button in the top bar. If you haven't created any projects yet, you'll be prompted to create one.

3. In the sidebar on the left, click on the "APIs & Services" button and then select "Credentials" from the menu.

4. Click on the "Create credentials" button, then select "OAuth client ID".

5. Select "Web application" as the application type, and enter a name for your application.

6. In the "Authorized JavaScript Origins" and "Authorized Redirect URIs" fields, enter the URLs of your application that will be handling the OAuth flow.
   In this project, "http://localhost:8000" is set as the "Authorized JavaScript Origins" and "http://localhost:8000/rest/v1/calendar/redirect" is set as the "Authorized Redirect URIs" field.

7. Click on the "Create" button.

8. Once the OAuth client ID has been created, you'll be able to see the client ID and client secret in the "Credentials" tab.

9. In the sidebar on the left, click on the "Library" button, then search for "Google Calendar API" and select it.

10. Click on the "Enable" button to enable the Google Calendar API for your project.

11. You can now use the client ID and client secret to authenticate with the Google Calendar API in your application.

Note: Make sure you keep your client secret private and don't share it publicly. Also, you should keep the client id and secret in a secure place, like in a secure environment variable, or in a secure file.

## Development Setup

1. Install Python and Django on your machine
2. Clone or download the project from the repository
3. Navigate to the project directory in the command line
4. Run the command `pip install -r requirements.txt` to install the project dependencies
5. Run the command `python manage.py makemigrations` to create the database tables
6. Run the command `python manage.py migrate` to apply the migrations to the database
7. Run the command `python manage.py runserver` to start the development server
8. Visit "http://127.0.0.1:8000/" in your web browser to see the project running
