# API Documentation

This documentation provides details about the Book and User APIs, which allow book management and user-related actions.
## How to run
Use a virtual environment and follow the setup
```
pip install -r requiremets.txt
python manage.py makemigrations
python manage.py migrate --run-syncdb
```
You can create an admin user with
```
python manage.py createsuperuser
```

To run use this command
```
python manage.py runserver
```
## User Endpoints

### 1. Register User

- **Endpoint:** `POST /api/user/register`
- **Description:** Register a new user in the system.

| Parameter    | Type   | Description                   |
| ------------ | ------ | ----------------------------- |
| `username`   | String | User's desired username       |
| `email`      | String | User's email address          |
| `password`   | String | User's password               |

### 2. Login User

- **Endpoint:** `POST /api/user/login`
- **Description:** Log in an existing user to obtain authentication tokens.

| Parameter    | Type   | Description                   |
| ------------ | ------ | ----------------------------- |
| `username`   | String | User's username               |
| `password`   | String | User's password               |

### 3. List Users

- **Endpoint:** `GET /api/user/list`
- **Description:** Retrieve a list of all registered users.

| Authentication Required | Admin Access Required |
| ------------------------ | ---------------------- |
| Yes                      | Yes                    |

### 4. View User Details

- **Endpoint:** `GET /api/user/view/<str:id>`
- **Description:** View details of a specific user by providing their user ID.

| Authentication Required | Admin Access Required |
| ------------------------ | ---------------------- |
| Yes                      | Yes                    |

## Book Endpoints

### 5. Add Book

- **Endpoint:** `POST /api/book/add`
- **Description:** Add a new book record to the library.

| Parameter          | Type   | Description                   |
| ------------------ | ------ | ----------------------------- |
| `title`            | String | Book title                    |
| `ISBN`             | String | International Standard Book Number |
| `genre`            | String | Book genre                    |
| `Published_date`   | Date   | Published date of the book    |

### 6. List All Books

- **Endpoint:** `GET /api/book/list`
- **Description:** Retrieve a list of all books in the library.

### 7. Get Book by ID

- **Endpoint:** `GET /api/book/get/<int:id>/`
- **Description:** Fetch details of a specific book by providing its Book ID.

### 8. Assign/Update Book Details

- **Endpoint:** `PUT /api/book/details/<int:id>/`
- **Description:** Assign details to a book or update existing book details.

| Parameter          | Type   | Description                   |
| ------------------ | ------ | ----------------------------- |
| `NumberOfPages`    | Int    | Number of pages in the book   |
| `language`         | String | Language of the book          |
| `publisher`        | String | Publisher of the book         |

### 9. Borrow a Book

- **Endpoint:** `POST /api/book/borrow/<int:id>/`
- **Description:** Record the borrowing of a book by linking a user with a book.

### 10. Return a Book

- **Endpoint:** `PUT /api/book/return/<int:id>/`
- **Description:** Update the system when a book is returned.

### 11. List All Borrowed Books

- **Endpoint:** `GET /api/book/list-borrowed/`
- **Description:** List all books currently borrowed from the library.

## How to Use

1. **Register User:** Send a POST request to `/api/user/register/` with the parameters: `username`, `email`, `password`.
2. **Login User:** Send a POST request to `/api/user/login` with the parameters: `username`, `password`. Obtain authentication tokens.
3. **List Users:** Send a GET request to `/api/user/list` with valid authentication tokens.
4. **View User Details:** Send a GET request to `/api/user/view/<str:id>` with valid authentication tokens.
5. **Add Book:** Send a POST request to `/api/book/add` with the parameters: `title`, `ISBN`, `genre`, `Published_date`.
6. **List All Books:** Send a GET request to `/api/book/list`.
7. **Get Book by ID:** Send a GET request to `/api/book/get/<int:id>`.
8. **Assign/Update Book Details:** Send a PUT request to `/api/book/details/<int:id>` with parameters: `NumberOfPages`, `language`, `publisher`.
9. **Borrow a Book:** Send a POST request to `/api/book/borrow/<int:id>/` with valid authentication tokens.
10. **Return a Book:** Send a PUT request to `/api/book/return/<int:id>/` with valid authentication tokens.
11. **List All Borrowed Books:** Send a GET request to `/api/book/list-borrowed/` with valid authentication tokens.

## Authentication and Permissions

- **User Actions:** Registration and login are open to the public. Other actions require authentication.
- **Admin Access:** Certain actions, such as viewing user details and listing users, require admin access in addition to authentication.
- **Token Usage:** Include authentication tokens obtained during login in the headers of authenticated requests.
