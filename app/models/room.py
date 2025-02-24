class Room:
    def __init__(self, id, name, capacity):
        self.id = id
        self.name = name
        self.capacity = capacity

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "capacity": self.capacity
        }