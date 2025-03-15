# Tic Tac Toe Game

A web-based implementation of the classic Tic Tac Toe game built with Flask, JavaScript, and PyScript. This project provides an interactive and fun way to play Tic Tac Toe against a bot or a friend.

## Features

- **Play with Bot or Friend**: Choose between playing against a simple AI bot or another player.
- **Flask Backend**: Handles game logic and API requests.
- **Dynamic UI**: The board updates dynamically using JavaScript.
- **Winner Announcement**: Displays the winner and highlights the winning cells.
- **Game Reset**: Restart the game easily from the menu.
- **Stylish UI**: Responsive and visually appealing interface with CSS animations.

## File Structure

```
├── app.py        # Flask backend handling game state and logic
├── templates
│   ├── index.html  # Frontend UI
├── static
│   ├── style.css   # Styles for the Tic Tac Toe game
│   ├── script.js   # JavaScript for handling frontend game logic
```

## Installation and Usage

### Prerequisites

- Python 3.x installed on your system.
- Flask installed (`pip install flask`).

### How to Run

#### Clone the Repository:
```sh
git clone https://github.com/YRMESHRAM/AI_tic-tac-toe.git
```

#### Navigate to the Project Directory:
```sh
cd AI_tic-tac-toe
```

#### Run the Flask Server:
```sh
python app.py
```

#### Open the Game in Browser:
Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## How to Play

1. Select a mode: Play against a bot or a friend.
2. Players take turns placing their marks (**X** or **O**) by clicking on the grid.
3. The first player to align three marks vertically, horizontally, or diagonally wins.
4. If all cells are filled without a winner, the game ends in a draw.
5. The game can be reset anytime from the menu.


## License

This project is licensed under the **MIT License**.

## Contact

For queries, suggestions, or collaborations:

- **GitHub**: [YRMESHRAM](https://github.com/YRMESHRAM)

