from flask import jsonify, request
from services.movie_service import fetch_movies, create_movie, delete_movie

def get_movies():
    movies = fetch_movies()
    return jsonify([movie.to_dict() for movie in movies]), 200

def add_movie():
    data = request.get_json()
    result, status_code = create_movie(data)
    return jsonify(result), status_code

def remove_movie(movie_id):
    result, status_code = delete_movie(movie_id)
    return jsonify(result), status_code