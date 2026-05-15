import json
from app.auth.jwt_handler import create_token

USER_FILE = "datasets/metadata/users.json"

def login(username, password):

    with open(USER_FILE) as f:
        users = json.load(f)

    for user in users:

        if (
            user["username"] == username
            and user["password"] == password
        ):

            token = create_token(
                {
                    "username": username,
                    "role": user["role"]
                }
            )

            return token

    return None