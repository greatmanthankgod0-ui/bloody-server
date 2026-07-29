# Bloody Server

A production-ready FastAPI backend providing authentication, user management, file uploads, and REST APIs.

---

# Architecture

```
                    Client
                       │
                 HTTP Request
                       │
                       ▼
               ┌──────────────┐
               │   FastAPI    │
               └──────┬───────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   Authentication   Users        Uploads
        │             │             │
        └─────────────┼─────────────┘
                      ▼
               Service Layer
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
 Authentication  User Service  File Service
                      │
                      ▼
             SQLAlchemy ORM
                      │
                      ▼
             SQLite Database
```

---

# Request Flow

```
Client
   │
   ▼
FastAPI Router
   │
   ▼
Service
   │
   ▼
Database
   │
   ▼
Response Wrapper
   │
   ▼
Client
```

---

# Authentication Flow

```
Register
   │
   ▼
Hash Password
   │
   ▼
Save User
   │
   ▼
Database
```

```
Login
   │
   ▼
Verify Password
   │
   ▼
Generate JWT
   │
   ▼
Return Token
```

---

# Protected Endpoint

```
Client
   │
Bearer Token
   │
   ▼
Security Middleware
   │
Decode JWT
   │
Load User
   │
Role Check
   │
Endpoint
```

---

# File Upload

```
Client
   │
Multipart File
   │
   ▼
Upload Endpoint
   │
Save File
   │
Return File Path
```

---

# Background Tasks

```
Request
   │
   ▼
Return Response
   │
   └──────────────┐
                  ▼
         Background Task
                  │
                  ▼
              Execute
```

---

# Project Structure

```
app/
├── api/
├── core/
├── database/
├── schemas/
├── services/
├── events/
└── main.py
```

---

# Technologies

- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- bcrypt
- Background Tasks
- Logging
- File Uploads
- Pagination
- Filtering
