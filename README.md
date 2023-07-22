# BlogApplication

In this web service we have tree app.

## 1-Accounts:
In this app have register view ,login view and profile view.
user can register to our web service and login to get an access token.
and for profile user can update their accounts details.

## 2-Blog:
here user can make a blog post and edited or deleted.
and user can rate to all blog posts.

## 3-Comment:
and at the end user can comment to all blog posts and edit and delete their comment or their blog post comments.

# service:
We have two service on docker for run this project.

## 1-MYSQL:
Our database and just need set some environment.

### .environment file
```
MYSQL_DATABASE=Your database name
MYSQL_USER=Your database user
MYSQL_PASSWORD=Your database password
MYSQL_ROOT_PASSWORD=Your database root user password
DATABASE_MYSQL_HOST=Your hostname
```
you should set this environment to -> 'mysql/.environment'

## 2-web:
this is our service and just need set some environment.

### .env file
```
SECRET_KEY=Your project secret key
MYSQL_DATABASE=Your database name
MYSQL_USER=Your database user
MYSQL_PASSWORD=Your database password
MYSQL_ROOT_PASSWORD=Your database root user password
DATABASE_MYSQL_HOST=Your hostname
PORT=Your project port
```
you should set this environment to -> '.env'

# Deploying
After you added .env file, you have to run the following commands to deploy the project:

```bash
docker-compose up --build -d
```

# [https://app.swaggerhub.com/apis-docs/ataattarian/BlogAPP/1.0.2-oas3]APIDocument

If there was any issue, contact me through [ata.attarian78@gmail.com](ata.attarian78@gmail.com) or [Telegram](https://telegram.me/ataattarian)