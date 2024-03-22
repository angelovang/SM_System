import uuid


def generate_unique_id():
    return str(uuid.uuid4().hex)[:8]
