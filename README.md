# bit.ly-like-service

## Backend

The backend service for the project.

**Tech**:
Bottlepy, Redis

### Backend API

Request:

Content-Type: application/json

body:

```json
{ "url": "http://google.com", "expires": 3000 }
```

Response:

```json
{ "code": 200, "error": {}, "data": {} }
```

| route                            | description       |
| -------------------------------- | ----------------- |
| /api/v1                          |                   |
| GET /healthcheck                 | Check the service |
| GET /get/:uid:re:[a-zA-Z0-9_]{6} | Get the real URL  |
| POST /create                     | Create a URL      |
