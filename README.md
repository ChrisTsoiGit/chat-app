# SafeChat - a social platform with secure chat & share

## About:

- Project name: SafeChat
- Time: 9/26/2022 - 10/227/2022
- Purposes:
  - demonstrate ability to use fastAPI in microservices
  - demonstrate ability to use MongoDB to ...
  - demonstrate ability to work with others in a team setting
- Team members & responsibilities:
  - Austin Miller: blog post and share
  - Chris Tsoi: contacts and contacts list
  - Echo Yang: user login/logout
  - Qingying Meng: chat and chats history

---

## Overview:

- Wire-frame diagram:
  ![Wire-frame diagrams](/images/wireframe.png)

- App preview:
  ![App preview](/images/LsJazlDzWa.gif)

---

## Getting started:

- Fork the repository at
- Add teammate to the project: GitLab > Project Information > Members > Invite members (as Maintainer)
- All member clone the same repo to their computer:
  ```
  git clone https://gitlab.com/chatapp12/chat-app.git
  ```

---

## Project setup:

### Virtual environment

- create virtual environment & activate:
  ```python
  python -m venv .venv
  source .venv/bin/activate
  ```
- update pip:
  ```python
  python -m pip install --upgrade pip
  ```
- install dependencies:
  ```python
  pip install -r requirements.txt
  ```

### Docker

create the sample-data volume before composing up:

```
docker volume create sample-data
docker compose build
docker compose up
docker image prune -a
```

### Working in dev branches:

1. creates a dev-branch:

   ```python
   (main) $ git checkout -b my-branch  # create and change to a new branch
   (my-branch) $  # <-- hey look, I'm in my new branch
   ```

2. push to the main branch, follow these steps:
   ![merging to main](/images/merge.png)

   ```python
   (my-branch) $ git add.
   (my-branch) $ git commit
   (my-branch) $ pit push             # 1. push to personal
   (my-branch) $ git checkout main    # 2. switch to main branch
   (main) $ git pull                  # 3. get latest from remote
   (main) $ git checkout my-branch    # 4. switch to dev branch
   (my-branch) $ git merge main       # 5. merge latest into dev branch
   ... handle any merging here
   ... test out your code
   (my-branch) $ git checkout main    # 6. switch to main branch
   (main) $ git pull                  #    test for changes on remote
   ... if no changes proceed,
   ... if changes go back to line 3
   (main) $ git merge my-branch       # 7. merge dev branch into main
   (main) $ git merge --abort         #    recall merge
   (main) $ git push                  #    push changes to the remote
   (main) $ git checkout my-branch    # 8. change back to dev branch
   ```

3. Merge conflicts

---

## Front-end:

---

## Back-end:

- start application by running uvicorn & start reloader and server process
  ```python
  uvicorn main:app --reload
  ```
  - open http://127.0.0.1:8000/ in browser
  - default FastAPI swagger page: http://127.0.0.1:8000/docs

### MongoDB CRUD operations:

- db.createCollection(collection_name, options)
- db.insertOne(data, options)
- db.insertMany(data, options)
- db.indOne(filter, options)
- db.find(filter, options)
- db.update(filter, data, options)
- db.updateOne(filter, data, options)
- db.updateMany(filter, data, options)
- db.replaceOne(filter, data, options)
- db.deleteOne(filter, options)
- db.deleteMany(filter, options)
- db.getCollectionInfos()

```bson
db.movies.insertOne({name: "Movie A", year: 1976})
db.movies.insertOne({name: "Movie B", year: 2001, cast: {director: "Joseph", actors: ["Kate", "Yuri", "Kai"]}})
db.movies.find(year: {$gt{1900}})
db.movies.find().pretty()
db.moovies.updateOne({year: 1976}, {$set: {marker: "delete"}})
db.moovies.updateOne({}, {$set: {marker: "toDelete"}})
db.movies.deleteOne({db.movies.deleteOne({})})
db.movies.deleteMany({marker: "toDelete"})
db.movies.deleteMany({})
```

---

## Deploy:

1. Setup and deploy group project template
2. Create Heroku account. Only one needed for the project, but all should create one and play with it.
3. Get Heroku API Key: Heroku avatar > Settings > API Key > Reveal
4. Create a Heroku application: upper right corner "New" > Create new app > App name: my-safe-chat
5. Set 2 env vars in `.gitlab-ci.yml`:
   - `PUBLIC_URL`: "https://USERNAME(qmeng222).gitlab.io/PROJECTNAME(safe-app)"
   - `REACT_APP_API_HOST`: "https://HEROKU-APP-NAME(my-safe-chat).herokuapp.com"
6. Set 2 env vars in `.gitlab-ci.yml`:
   - `PUBLIC_URL`: "https://USERNAME(qmeng222).gitlab.io/PROJECTNAME(safe-app)"
   - `REACT_APP_API_HOST`: "https://HEROKU-APP-NAME(my-safe-chat).herokuapp.com"
7. Set Heroku Config Variables:
   Heroku app name > Settings > Config Vars > Reveal Config Vars > Add
   - CORS_HOST (as key): "https://USERNAME.gitlab.io" (as value)
8. Set GitLab CI/CD Variables (Settings > CI/CD > Variables > Expand > Add variables, one by one):
   - HEROKU_API_KEY: value from step #2 above. This must be "masked" and "protected".
   - HEROKU_FASTAPI_APP: HEROKU_APP_NAME
   - REACT_APP_API_HOST: "https://HEROKU_APP-NAME.herokuapp.com"
9. Push to main, go watch the CI/CD pipeline in gitlab
10. When that succeeds, go see if your site is up: Settings > Pages > click the link

---

The following project files have created as a minimal starting point. Please follow the guidance for each one for a most successful project.

- `docker-compose.yaml`: there isn't much in here, just a **really** simple UI. Add services to this file as you did with previous projects in module #2.
- `.gitlab-ci.yml`: This is your "ci/cd" file where you will configure
  automated unit tests, code quality checks, and the building and deployment
  of your production system. Currently, all it does is deploy an
  "under construction" page to your production UI on GitLab. We will learn
  much more about this file
- `.gitignore`: don't keep track of things you don't need to like
  `node_modules`, `__pycache__`, etc.

## How to complete the initial deploy

There will be further guidance on completing the initial deployment, but it just consists of these steps:

- setup Heroku account and app
- setup 2 CI/CD variables in GitLab
- push to main
