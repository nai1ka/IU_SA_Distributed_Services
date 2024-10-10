import requests
from typing import List


feed_service_url = "http://127.0.0.1:5001"
message_service_url = "http://127.0.0.1:5002"
user_service_url = "http://127.0.0.1:5003"


def register(session: requests.Session, command: List[str]) -> str | None:
    if len(command) != 2:
        print("Invalid command args. Type `help` for commands.")
        return
    try:
        response = session.post(
            url=user_service_url + "/users/register",
            json={"username": command[1]},
        )
        response.raise_for_status()
        return command[1]
    except requests.exceptions.ConnectionError:
        print("Could not connect to the user service")
    except requests.exceptions.RequestException:
        print("Failed to register:", response.text.strip())


def login(command: List[str]) -> str:
    if len(command) != 2:
        print("Invalid command args. Type `help` for commands.")
        return
    return command[1]


def send(session: requests.Session, command: List[str], username: str | None):
    if len(command) < 2:
        print("Invalid command args. Type `help` for commands.")
        return
    if username is None:
        print("Username is not set. Register first. Type `help` for commands.")
        return
    try:
        response = session.post(
            url=message_service_url + "/messages",
            json={"username": username, "content": " ".join(command[1:])},
        )
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("Could not connect to the message service")
    except requests.exceptions.RequestException:
        print("Failed to send message:", response.text.strip())


def like(session: requests.Session, command: List[str], username: str | None):
    if len(command) != 2:
        print("Invalid command args. Type `help` for commands.")
        return
    if username is None:
        print("Username is not set. Register first. Type `help` for commands.")
        return
    try:
        response = session.post(
            url=message_service_url + f"/messages/{command[1]}/like",
            json={"username": username},
        )
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("Could not connect to the message service")
    except requests.exceptions.RequestException:
        print("Failed to like/unlike message:", response.text.strip())


def feed(session: requests.Session):
    try:
        response = session.get(url=feed_service_url + "/feed")
        response.raise_for_status()
        for msg in response.json():
            print(
                f"[Username={msg['username']}, MessageID={msg['message_id']}, "
                f"Likes={msg['num_of_likes']}] {msg['content']}"
            )
    except requests.exceptions.ConnectionError:
        print("Could not connect to the feed service")
    except requests.exceptions.RequestException:
        print("Failed to get the feed:", response.text.strip())


def _help():
    print("- register <USERNAME>: Register the user with the following username.")
    print("- login <USERNAME>: Login into the user with the following username.")
    print("- send <TEXT>: Send the post with the following text.")
    print("- like <ID>: Like/unlike the post with the following ID. Liking an already liked post unlikes it.")
    print("- feed: Get the feed (last 10 messages).")
    print("- exit: Exit the interface.")


def main() -> None:
    session = requests.Session()
    username: str | None = None

    while True:
        command = input("> ").split()

        if not command:
            print("Invalid command. Type `help` for commands.")
            continue

        match command[0]:
            case "register":
                username = register(session, command)
            case "login":
                username = login(command)
            case "send":
                send(session, command, username)
            case "like":
                like(session, command, username)
            case "help":
                _help()
            case "feed":
                feed(session)
            case "exit":
                break
            case _:
                print("Invalid command. Type `help` for commands.")


if __name__ == "__main__":
    main()
