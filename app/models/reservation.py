class Reservation:
    def __init__(self, id, function, email, seats):
        self.id = id
        self.function = function
        self.email = email
        self.seats = seats

    def to_dict(self):
        return {
            "id": self.id,
            "function": self.function,
            "email": self.email,
            "seats": self.seats
        }