# IU_SA_Distributed_Services

## Team members

Team 24:

- Gleb Bugaev ([g.bugaev@innopolis.university](mailto:g.bugaev@innopolis.university))
- Nail Minnemullin ([n.minnemullin@innopolis.university](mailto:n.minnemullin@innopolis.university))
- Dmitriy Okoneshnikov ([d.okoneshnikov@innopolis.university](mailto:d.okoneshnikov@innopolis.university))
- Vladislav Bolshakov ([v.bolshakov@innopolis.university](mailto:v.bolshakov@innopolis.university))

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
