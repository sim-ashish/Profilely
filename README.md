# Profilely README

Profilely is a api project where user can create their profiles and manage them

---

## Table of Contents

- [Features](#features)
- [URL Structure](#url-structure)
- [Authentication and Authorization](#authentication-and-authorization)



---

## Features

- **Account Creation**: User can create their accounts
- **Verify Account**: User can verify their accout by email link, after that only account is visible
- **Login**: After verification, user can login into their account using email and password
- **My Profile**: User can see their profile after login
- **All users**: Can see all users, admin can see some extra fields
- **Specific User**: Get specific user details using id
- **Delete User**: user can delete his profile, admin can delete anyone's account
- **Reset password**: user can reset their password, after login only
- **forgot password**: user can reset their forgot password, using mail link
- **PostgreSQL Database**: Relational database system for data storage.
- **Frontend Integration**: DRF templated views for easy integration with frontend applications.

---

## URL Structure

The project exposes several key API endpoints. Below is the list of primary URL patterns:

### User  (`/user/`)
| Method | Endpoint | Description |
|--------|----------|-------------|
|GET |	`/user/me` |	Get current loggedIn user
|GET |	`/user/verify` |	verify user
|GET |	`/user/all` |	Get all verified users
|GET |	`/user/{user_id}` |	Get specific verified user
|POST |	`/user/` |	Create a new user
|POST |	`/user/login` |	login user
|POST |	`/user/forgot-password` |	forgot password(this will send link to email)
|POST |	`/user/reset-forgot-password` |	reset-forgot-password (this will change the password)
|POST |	`/user/reset-password` |	reset-password
|PATCH |`/user/{user_id}` |	Update a specific user
|DELETE |   `/user/{user_id}`	| Delete a specific user

## Authentication and Authorization

Profilely supports Jwt token authentication:

- admin have all the access
- user have all access to its account only