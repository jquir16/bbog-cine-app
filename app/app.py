from flask import Flask
from flask_cors import CORS
from controllers.movie_controller import get_movies, create_movie, update_movie, delete_movie

app = Flask(__name__)
CORS(app)

app.config['ERROR_404_HELP'] = False

@app.route('/movies', methods=['GET'])
def list_movies():
    return get_movies()

@app.route('/movies', methods=['POST'])
def add_movie():
    return create_movie()

@app.route('/movies/<int:movie_id>', methods=['PUT'])
def modify_movie(movie_id):
    return update_movie(movie_id)

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def remove_movie(movie_id):
    return delete_movie(movie_id)

def main():
    app.run()

if __name__ == '__main__':
    main()