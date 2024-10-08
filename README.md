# IU_SA_Distributed_Services

## Team members

Team 24:

- Gleb Bugaev ([g.bugaev@innopolis.university](mailto:g.bugaev@innopolis.university))
- Nail Minnemullin ([n.minnemullin@innopolis.university](mailto:n.minnemullin@innopolis.university))
- Dmitriy Okoneshnikov ([d.okoneshnikov@innopolis.university](mailto:d.okoneshnikov@innopolis.university))
- Vladislav Bolshakov ([v.bolshakov@innopolis.university](mailto:v.bolshakov@innopolis.university))
## System Desctiption

<a href="https://drive.google.com/uc?export=view&id=<FILEID>"><img src="https://drive.google.com/uc?export=view&id=1boY0wn0ZUHPNs7Q-U--jwBelMK2HlOuL" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />

Our system has a service-based architecture style. It consists of a user interface, one database and 3 services that do not contact each other and that are splitted based on business requirements.

**User Service:**

&emsp;&emsp;Responsible for all actions regarding users’ accounts, such as registration and login.

**Message Service:**

&emsp;&emsp;Responsible for creating new messages and sending them to the database. Also, this service allows users to like and unlike messages.

**Feed Service:**

&emsp;&emsp;Responsible for showing a feed of the last 10 messages to the users.

## Separation by Services

We decided to split the whole system by these 3 services due to business requirements and logic of future possible scaling. 

**User Service** covers a business requirement about users ability to register new accounts and post messages only if they are registered. With the growth of users number, this service can be scaled by creating new workers responsible for simultaneous registration of users and login processes.

**Message Service** covers a business requirement about users ability to post short messages and like or unlike messages. It can be scaled creating new workers and supporting parallel or very fast writes to the database.

**Feed Service** covers a business requirement about users ability to read messages by seeing the last 10 posted messages as a feed. Need of scaling can arise when the number of messages becomes larger. It can be done by adding caching of the last messages that was read by the service from a database.

## Endpoints

`POST /users/register` - register a new user
Takes a JSON object with the following fields:
```json
{
    "username" : "johndoe"
}
```

----

`GET /feed` - get a feed of all posts

----

`POST /messages` - send a message
Takes a JSON object with the following fields:

```json
{
    "username" : "johndoe",
    "context" : "Hello, world!",
}
```

----

`POST /messages/<int:id>/like` - like a message
Takes a JSON object with the following fields:

```json

{
    "username" : "johndoe"
}
```

If the user has already liked the message, the like will be removed.
