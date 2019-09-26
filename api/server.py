from flask import Flask, jsonify, request
from flask_cors import CORS # allow communication with react app
from game import Game

app = Flask(__name__)
CORS(app)

@app.route('/new')
def new_board():
    game = Game()
    game.randomize()
    return jsonify(game.board)

@app.route('/next', methods=['POST'])
def next_board():
    game = Game(request.json['board'])
    game.tick()
    return jsonify(game.board)

if __name__ == '__main__':
    app.run()
