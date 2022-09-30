## API Design:

<br>

### 1. Create a post:

- Endpoint path: /Moments
- Endpoint method: POST

- Headers:

  - Authorization: Bearer token

- Request body:

  ```json
  {
    "post": [
        {
        "avatar_url": string,
        "contact_name": string,
        "post_text": string,
        "image_url": string,
        "video_url": string,
        "time_stamp": string,  <!-- "2022-10-01" ?????? -->
      }
    ]
  }
  ```

- Response: An indication of success or failure
- Response shape:
  ```json
  {
    "success": boolean,
    "message": string
  }
  ```

<br>

### 2. [stretch goal] Moments - list of posts:

- Endpoint path: /moments
- Endpoint method: GET

- Headers:

  - Authorization: Bearer token

- Response: A list of posts
- Response shape:

  ```json
  {
    "moments": [
      {
        "avatar_url": string,
        "contact_name": string,
        "post_text": string,
        "image_url": string,
        "video_url": string,
        "time_stamp": string,
        "likes": number
      }
    ]
  }
  ```

---

<br>

## Required Endpoints:

<br>

### 1. Log in:

- Endpoint path: /token
- Endpoint method: POST

- Request shape (form):

  - username: string
  - password: string

- Response: Account information and a token
- Response shape (JSON):

  ```json
  {
    "account": {
        "username": string,
        "password": string,
    },
    "token": string  <!-- ??????? -->
  }
  ```

<br>

### 2. Log out:

- Endpoint path: /token
- Endpoint method: DELETE

- Headers:

  - Authorization: Bearer token

- Response: Always true
- Response shape (JSON):

  ```json
  true
  ```

---

<br>

## Endpoint Template:

<br>

- [x] Use the following template to describe each of your endpoints.
- [x] Everything between the guillemots (« and ») should be replaced by you to describe the endpoint.
- [x] Mandatory fields are:
  - Endpoint path
  - Endpoint method
  - Response
  - Response shape
- [x] Optional fields:
  - If your endpoint needs to know who the person is, then include the **_Headers/Authorization_** part.
  - If your endpoint is a POST, PUT, or PATCH, include the Request shape (JSON) part.

<br>

- Endpoint path: «path to use»
- Endpoint method: «HTTP method»
- Query parameters:

  - «name»: «purpose»

- Headers:

  - Authorization: Bearer token

- Request shape (JSON):

  ```json
  «JSON-looking thing that has the
  keys and types in it»
  ```

- Response: «Human-readable description
  of response»
- Response shape (JSON):
  ```json
  «JSON-looking thing that has the
  keys and types in it»
  ```
