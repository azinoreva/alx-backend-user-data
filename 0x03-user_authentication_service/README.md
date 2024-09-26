User Authentication Service
Description
This project implements a user authentication system using SQLAlchemy for ORM and Flask for API handling. It provides functionality for user management, including creating users, updating user information, handling sessions, and password management.

The repository includes tasks that gradually build up a complete authentication service, from creating a user model to implementing a login system.

Technologies
Python 3.x
SQLAlchemy
Flask
SQLite
bcrypt
Features
User Model: A SQLAlchemy model to represent users.
Create User: Add new users to the database with hashed passwords.
Find User: Search for users in the database based on arbitrary keyword arguments.
Update User: Modify user attributes.
Password Hashing: Secure password storage using bcrypt.
User Registration: Add new users via API and ensure unique emails.
Flask API: A simple API to handle user login, session creation, and logout.
UUID-based Sessions: Implement session management using UUIDs.
Authentication Validation: Validate user credentials securely with bcrypt.
Files
user.py
Contains the User model:

id: Integer primary key.
email: Non-nullable string.
hashed_password: Non-nullable string.
session_id: Nullable string for user sessions.
reset_token: Nullable string for password resets.
db.py
Manages database operations:

DB class: Responsible for interacting with the database.
add_user(email, hashed_password): Adds a new user.
find_user_by(**kwargs): Retrieves a user based on filters.
update_user(user_id, **kwargs): Updates user attributes.
auth.py
Handles authentication-related logic:

Auth class: Manages authentication operations.
register_user(email, password): Registers a new user, raises error if email is taken.
_hash_password(password): Returns a bcrypt hashed password.
valid_login(email, password): Validates login credentials.
create_session(email): Generates and stores a session ID.
get_user_from_session_id(session_id): Retrieves user from session ID.
destroy_session(user_id): Logs user out by clearing session ID.
app.py
Sets up the Flask application with routes:

GET /: Returns a welcome message in JSON format.
POST /users: Registers a new user.
POST /sessions: Logs a user in, sets session ID cookie.
DELETE /sessions: Logs a user out by destroying the session.
