# Annuaire API

The Annuaire API is a simple REST API for managing users in a directory. It allows you to add, delete, and authenticate users.

## Usage

To use this API, you can send HTTP requests to the appropriate endpoints.

### Endpoints

#### Get the list of users

GET http://localhost:8080/api/users

This endpoint will return the list of user names in the directory.

### Add a user

POST http://localhost:8080/api/add
Content-Type: application/json

{
  "login": "new_user",
  "password": "password"
}

This endpoint allows you to add a new user to the directory by providing their username and password.

### Authentication

POST http://localhost:8080/api/authenticate
Content-Type: application/json

{
  "login": "user",
  "password": "password"
}

This endpoint allows you to authenticate a user by checking their username and password. If authentication succeeds, the user receives an authentication token.

### Delete a user

DELETE http://localhost:8080/api/delete?login=user

This endpoint allows you to delete a user from the directory by providing their username.

### Logout

POST http://localhost:8080/api/logout

This endpoint allows you to log out a user by invalidating their session.

### Running the API
To run the API, you can deploy the application to your preferred Jakarta EE server. You will also need to configure a database server to store users.

### Configuration
The API configuration can be found in the META-INF/persistence.xml file. You will need to configure the data source (DataSource) for your database in this file.
