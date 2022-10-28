# Module3 Project Gamma-Chatroom App

- Austin Miller
- Chris Tsoi
- Echo Yang
- Qingying Meng

## Intended market
![GIF](/image/main.gif)

Vintage classic chatroom which bring you back to the old time where everyone can gathering together in the same channel to exchange all their ideas. Great for making new friends! 

## Design

User Interface

![merging to main](/image/planning.png)

 Docker Network

![merging to main](/image/docker.png)
- User can register on the registration page using username, email and password.
- Pre registered can access the chatroom by using the sign up page.
- Non-registered users is not allowed to access to the chatroom.
- The chatroom can support multi logged in users chatting in the same room at the same time.

  [API design](https://gitlab.com/chatapp12/chat-app/-/blob/main/docs/api%20design.md)

  [data models](https://gitlab.com/chatapp12/chat-app/-/blob/main/docs/data%20model.md)

  [ghi](https://gitlab.com/chatapp12/chat-app/-/blob/main/docs/ghi.md)



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

### Unit tests for group members


Austin:

Chris: test_create_acct_chris.py

Echo: test_get_token_echo.py

Qingying: test_get_blog_qingying.py



### Instrutions for starting a new chat in our public chatroom 
Go to https://chatapp12.gitlab.io/chat-app/chat You will need to sign up first then log in to your account use your user name and password. Once you get into the chatroom,type in your words and press "send".



## How to complete the initial deploy

There will be further guidance on completing the initial deployment, but it just consists of these steps:

- setup Heroku account and app
- setup 2 CI/CD variables in GitLab
- push to main
