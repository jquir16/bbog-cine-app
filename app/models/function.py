class Function:
    def __init__(self, id, movie, room, time):
        self.id = id
        self.movie = movie
        self.room = room
        self.time = time

    def to_dict(self):
        return {
            "id": self.id,
            "movie": self.movie,
            "room": self.room,
            "time": self.time
        }