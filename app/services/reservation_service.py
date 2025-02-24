from utils.database_connection import execute_query
from models.reservation import Reservation

def fetch_reservations():
    query = "SELECT * FROM reservations"
    reservations_data = execute_query(query, fetch=True)
    if reservations_data is None:
        return []
    return [Reservation(*reservation_data) for reservation_data in reservations_data]

def get_room_capacity(function_id):
    query = """
    SELECT r.capacity
    FROM rooms r
    JOIN functions f ON r.id = f.room
    WHERE f.id = %s;
    """
    result = execute_query(query, (function_id,), fetch=True)
    if not result:
        return None
    return result[0][0]

def get_reserved_seats(function_id):
    query = """
    SELECT COALESCE(SUM(seats), 0)
    FROM reservations
    WHERE function = %s;
    """
    result = execute_query(query, (function_id,), fetch=True)
    return int(result[0][0]) if result else 0

def create_reservation(function_id, email, seats):
    try:
        room_capacity = get_room_capacity(function_id)
        if room_capacity is None:
            return {"error": "Room not found for the given function"}, 404
        
        reserved_seats = get_reserved_seats(function_id)
        
        if reserved_seats + int(seats) > room_capacity:
            return {"error": "The number of seats exceeds the room capacity"}, 400
        
        query = """
        INSERT INTO public.reservations (function, email, seats) VALUES (%s, %s, %s) RETURNING *;
        """
        reservation_data = execute_query(query, (function_id, email, seats), fetch=True)
        if reservation_data:
            reservation = Reservation(*reservation_data[0])
            return reservation.to_dict(), 201
        else:
            return {"error": "Failed to insert reservation"}, 500
    except Exception as e:
        print(f"Error inserting reservation: {e}")
        return {"error": "An error occurred while inserting the reservation"}, 500