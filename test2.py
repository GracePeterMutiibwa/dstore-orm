import uuid

def randomIdGenerator():
    return str(uuid.uuid4())

print(randomIdGenerator())