# Module3 Project Gamma-Chatroom App

- Austin Miller
- Chris Tsoi
- Echo Yang
- Qingying Meng

## Intended market

Vintage classic chatroom which bring you back to the old time where everyone can gathering together in the same channel to exchange all their ideas. Great for making new friends! 

## Design
![merging to main](/image/planning.png)
- User can register on the registration page using username, email and password.
- Pre registered can access the chatroom by using the sign up page.
- Non-registered users is not allowed to access to the chatroom.
- The chatroom can support multi logged in users chatting in the same room at the same time.

## Project Setup

1. Visit this [Chatroom](https://gitlab.com/chatapp12/chat-app.git) repository.
2. Click the blue clone button and copy the URL under the Clone with HTTPS.
3. Open the terminal and change(cd) to a directory where to store this application(Chatroom).
4. Type ***git clone*** and paste the URL cloned in step 2.
5. After the application is cloned locally, change(cd) the directories into the application(Chatroom) directory.
6. Install and Open Docker Desktop.
7. In the terminal, type ***docker-compose build*** to build Docker image.
8. Type ***docker volume create mongo-data*** to create the volume.
9. Type ***docker-up build*** to run the cotainers.
 10. Type http://localhost:3000 in the browser, and explore the Chatroom log in page.

### Directories

Several directories have been added to your project. The directories `docs` and `journals` are places for you and your team-mates to, respectively, put any documentation about your project that you create and to put your project-journal entries. See the README file in each directory for more info.

The other directories, `ghi` and `sample_service`, are sample services, that you can start building off of or use as a reference point.

Inside of `ghi` is a minimal React app that has an "under construction" page. It is setup similarly to all of the other React projects that you have worked on.

Inside of `sample_service` is a minimal FastAPI application. "Where are all the files?" you might ask? Well, the `main.py` file is the whole thing, and go take look inside of it... There's not even much in there..., hmm? That is FastAPI, we'll learn more about it in the coming days. Can you figure out what this little web-application does even though you haven't learned about FastAPI yet?

### Other files

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
