from utils.database_connection import execute_query
from models.movie import Movie

def fetch_movies():
    query = "SELECT * FROM movies"
    movies_data = execute_query(query, fetch=True)
    if movies_data is None:
        return []
    return [Movie(*movie_data) for movie_data in movies_data]

def create_movie(data):
    query = """
        INSERT INTO movies (title, overview, director, casting, release_date, start_date, end_date, runtime, mpaa)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *;
    """
    params = (data['title'], data.get('overview'), data.get('director'), data.get('casting'), data['release_date'], data['start_date'], data.get('end_date'), data['runtime'], data['mpaa'])
    movie_data = execute_query(query, params, fetch=True)
    if movie_data:
        return Movie(*movie_data[0]).to_dict(), 201
    else:
        return {"error": "Error creating movie"}, 400

def delete_movie(movie_id):
    query = "DELETE FROM movies WHERE id = %s RETURNING *;"
    params = (movie_id,)
    movie_data = execute_query(query, params, fetch=True)
    if movie_data:
        return {"message": "Movie deleted successfully"}, 200
    else:
        return {"error": "Error deleting movie"}, 400