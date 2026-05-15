import json

PERMISSION_FILE = "datasets/metadata/permissions.json"

def check_access(role, document_name):

    with open(PERMISSION_FILE) as f:
        permissions = json.load(f)

    allowed_roles = permissions.get(document_name, [])

    return role in allowed_roles