from flask import jsonify, request
from services.reservation_service import fetch_reservations, create_reservation

def get_reservations():
    reservations = fetch_reservations()
    return jsonify([reservation.to_dict() for reservation in reservations]), 200

def insert_reservation():
    data = request.get_json()
    function_id = data.get('function')
    email = data.get('email')
    seats = data.get('seats')
    
    print(f"Received data: function_id={function_id}, email={email}, seats={seats}")
    
    if not function_id or not email or not seats:
        return jsonify({"error": "Missing function, email, or seats"}), 400
    
    result, status_code = create_reservation(function_id, email, seats)
    return jsonify(result), status_code