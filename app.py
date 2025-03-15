from flask import Flask, request, jsonify, render_template
import random


app = Flask(__name__)

# Game state
class GameState:
    def __init__(self):
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.current_player = "X"
        self.game_mode = "bot"  # "bot" or "friend"
        self.game_ended = False

    def reset(self, mode="bot"):
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.current_player = "X"
        self.game_mode = mode
        self.game_ended = False

state = GameState()

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0], [(i, 0), (i, 1), (i, 2)]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i], [(0, i), (1, i), (2, i)]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0], [(0, 0), (1, 1), (2, 2)]
    if board[2][0] == board[1][1] == board[0][2] != "":
        return board[2][0], [(2, 0), (1, 1), (0, 2)]
    return None, None

def check_draw(board):
    return all(cell != "" for row in board for cell in row)

def ai_move(board):
    best_move = get_best_move(board)
    if best_move:
        x, y = best_move
        board[x][y] = "O"

def get_best_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                if check_winner(board)[0] == "O":
                    board[i][j] = ""
                    return (i, j)
                board[i][j] = ""
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "X"
                if check_winner(board)[0] == "X":
                    board[i][j] = ""
                    return (i, j)
                board[i][j] = ""
    if board[1][1] == "":
        return (1, 1)
    for x, y in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if board[x][y] == "":
            return (x, y)
    empty_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    return random.choice(empty_spots) if empty_spots else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    x, y = data['x'], data['y']

    if state.game_ended:
        return jsonify({"status": "game_over", "board": state.board})

    if state.board[x][y] == "":
        # Update the board with the current move
        state.board[x][y] = state.current_player

        # Check for a winner after the move
        winner, winning_cells = check_winner(state.board)
        
        if winner:
            # If there's a winner, mark the game as ended
            state.game_ended = True
            return jsonify({
                "status": "win",
                "winner": winner,
                "board": state.board,
                "winning_cells": winning_cells
            })

        # Check for a draw
        if check_draw(state.board):
            state.game_ended = True
            return jsonify({
                "status": "draw",
                "board": state.board
            })

        # Switch the current player
        state.current_player = "O" if state.current_player == "X" else "X"

        # Bot move if in bot mode and the bot's turn
        if state.game_mode == "bot" and state.current_player == "O":
            
       
            ai_move(state.board)
            winner, winning_cells = check_winner(state.board)
            
            if winner:
                state.game_ended = True
                return jsonify({
                    "status": "win",
                    "winner": winner,
                    "board": state.board,
                    "winning_cells": winning_cells
                })

            if check_draw(state.board):
                state.game_ended = True
                return jsonify({
                    "status": "draw",
                    "board": state.board
                })

            state.current_player = "X"

        return jsonify({
            "status": "continue",
            "board": state.board,
            "current_player": state.current_player
        })

    return jsonify({
        "status": "invalid",
        "board": state.board
    })

@app.route('/reset', methods=['POST'])
def reset():
    mode = request.json.get("mode", "bot")
    state.reset(mode)
    return jsonify({"status": "reset", "board": state.board, "current_player": state.current_player})

if __name__ == '__main__':
    app.run(debug=True)
