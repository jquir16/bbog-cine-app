from flask import jsonify
from services.rooms_service import fetch_rooms

def get_rooms():
    rooms = fetch_rooms()
    if not rooms:
        return jsonify([]), 404
    return jsonify([room.to_dict() for room in rooms]), 200