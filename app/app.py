from flask import Flask
from flask_cors import CORS
from controllers.movie_controller import get_movies, create_movie
from controllers.reservation_controller import get_reservations, insert_reservation
from controllers.rooms_controller import get_rooms

app = Flask(__name__)
CORS(app)

app.config['ERROR_404_HELP'] = False

@app.route('/movies', methods=['GET'])
def list_movies():
    return get_movies()

@app.route('/movies', methods=['POST'])
def add_movie():
    return create_movie()

@app.route('/reservations', methods=['GET'])
def list_reservations():
    return get_reservations()

@app.route('/reservations', methods=['POST'])
def add_reservation():
    return insert_reservation()

@app.route('/rooms', methods=['GET'])
def list_rooms():
    return get_rooms()

def main():
    app.run()

if __name__ == '__main__':
    main()