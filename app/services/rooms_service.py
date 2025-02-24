from utils.database_connection import execute_query
from models.room import Room

def fetch_rooms():
    query = "SELECT * FROM rooms"
    rooms_data = execute_query(query, fetch=True)
    if rooms_data is None:
        return []
    return [Room(*room_data) for room_data in rooms_data]