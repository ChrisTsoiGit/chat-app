# Developer's Journal

## Template:

- The date of the entry
- A list of features/issues that you worked on and who you worked with, if applicable
- A reflection on any design conversations that you had
- At least one ah-ha! moment that you had during your coding, however small

---

## Tuesday, 10/11/2022

## Monday, 10/10/2022

- Edited the Dockerfile & defined services in the compose file
- Experimented MongoDB CRUD operations
- Ah-ha! moment: MongoDB enforces no schemas. Documents don't have to use the same schema inside of one collection.

<br>

## Friday off, 10/7/2022

- Learnt developing CRUD application using FastAPI & MongoDB

<br>

## Thursday, 10/6/2022

- updatd ReadMe with responsibilities assigned for each team member, plus MongoDB CRUD operations
- worked on data schemas and data modelling
- Ah-ha! moment: in MongoDB, we can build one-to-many relationsuse using references (e.g. \_id) or using embedded structure

## Wednesday, 10/5/2022

- Created _issues list_ for the work that we want to implement with group agreements.
- Wrote _user story_, _feature_, and _description_ for issue **_Chat_** and issue **_Chats history_**
- Ah-ha! moment: acceptance testing provides a clear and unambiguous “contract” between developers, complementing the unit tests.

<br>

## Tuesday, 10/4/2022

- Added a merge flowchat as well as detailed instructions to ReadMe.
- Disscussed project architecture to coordinate team work. I was assigned to implement the **_chat_** model and related features.
- Created my developer's journal and will log on daily basis
- Finished project setup:
  - Worked on creating Dockerfile and docker-compose.yaml file
  - created .gitattributes file in the top-level directory and editted it with configuration for supporting Windows users/collaborators, if any;
  - created and editted _create-multiple-databases.sh_ to support multiple database instances in a single PostgreSQL RDBMS;
  - add additional directories or files to project structure following instructions in Learn;
  - updatd docker-compose.yaml following instructions in Learn;
- Ah-ha! moment - PostgreSQL vs. MongoDB:
  - Postgres uses SQL; MongoDB uses BSON (NoSQL)
  - Postgres is a relational database management system; MongoDB is a document database.
  - A row in a table has to comply with the data types of the columns. A document can hold any data as key-value pairs.
  - PostgreSQL has a monolithic architecture; MongoDB has a distributed architecture.

<br>

## Monday, 10/3/2022

- Updated ReadMe.md with instructions for installing virtualEnv and FastAPI
- Updated project wirefram to v.3.
- Embedded wirefram.png into ReadMe.md (under _Overview_)
- Finished deployment with the help from team member Chris
- Updated ReadMe.md with detailed deployment instructions
- Pushed completed .gitlab-ci.yml file to my dev-branch for record
- Ah-ha! moment: GitLab project visualbitliy must be set to "public" to allow deployment

<br>

## Sunday, 10/2/2022

- Updated api-design.md to v.2. with corrected data types
- Labelled uncertain data types for further discussion with team members
- Updated project wireframe to v.2. with rearranged layouts

<br>

## Friday, 9/30/2022

- Discussed project topic & details with team members
- Created a live collaboration on Excalidraw at https://excalidraw.com/#room=39a092e7d8562776c544,Hv4ProKb7q01V6opLyDHqg
- Setup a dev-branch called **_qingying_**
- Finished project wirefram v.1.
- Created and finished api-design.md v.1.
- Ah-ha! moment:
  - failed to push to dev-branch (pipeline: failed)
  - solution: git push worked once GitLab account verification is finished
