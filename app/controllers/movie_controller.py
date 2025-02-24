from utils.database_connection import execute_query 
from models.movie import Movie
from flask import jsonify, request

def fetch_movies():
    query = "SELECT * FROM movies"
    movies_data = execute_query(query, fetch=True)
    if movies_data is None:
        return []
    return [Movie(*movie_data) for movie_data in movies_data]

def get_movies():
    movies = fetch_movies()
    return jsonify([movie.to_dict() for movie in movies])

def create_movie():
    data = request.get_json()
    query = """
        INSERT INTO movies (title, overview, director, casting, release_date, start_date, end_date, runtime, mpaa)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    params = (data['title'], data.get('overview'), data.get('director'), data.get('casting'), data['release_date'], data['start_date'], data.get('end_date'), data['runtime'], data['mpaa'])
    result = execute_query(query, params)
    if result is None:
        return jsonify({"error": "Error creating movie"}), 400
    return jsonify({"message": "Movie created successfully"}), 201

def update_movie(movie_id):
    data = request.get_json()
    query = """
        UPDATE movies
        SET title = %s, overview = %s, director = %s, casting = %s, release_date = %s, start_date = %s, end_date = %s, runtime = %s, mpaa = %s
        WHERE id = %s
    """
    params = (data['title'], data.get('overview'), data.get('director'), data.get('casting'), data['release_date'], data['start_date'], data.get('end_date'), data['runtime'], data['mpaa'], movie_id)
    result = execute_query(query, params)
    if result is None:
        return jsonify({"error": "Error updating movie"}), 400
    return jsonify({"message": "Movie updated successfully"}), 200

def delete_movie(movie_id):
    query = "DELETE FROM movies WHERE id = %s"
    params = (movie_id,)
    result = execute_query(query, params)
    if result is None:
        return jsonify({"error": "Error deleting movie"}), 400
    return jsonify({"message": "Movie deleted successfully"}), 200