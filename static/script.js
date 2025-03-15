let currentPlayer = "X";
let gameMode = "bot";
let gameEnded = false;  // Track if the game has ended

function createBoard() {
    const boardElement = document.getElementById("board");
    boardElement.innerHTML = "";
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const cell = document.createElement("div");
            cell.dataset.x = i;
            cell.dataset.y = j;
            cell.onclick = () => makeMove(i, j);
            boardElement.appendChild(cell);
        }
    }
}

async function makeMove(x, y) {
    if (gameEnded || document.querySelector(`[data-x='${x}'][data-y='${y}']`).textContent) return;

    const response = await fetch("/move", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ x, y }),
    });
    const data = await response.json();

    // Update the board with the new state
    updateBoard(data.board);

    // Toggle currentPlayer and update the turn indicator
    currentPlayer = currentPlayer === "X" ? "O" : "X";
    document.getElementById("turn-indicator").textContent = `Player ${currentPlayer}'s turn`;

    // Delay the display of the result to ensure the last move is visible
    setTimeout(() => {
        if (data.status === "win") {
            alert(`Player ${data.winner} wins!`);
            highlightWinningCells(data.winning_cells);
            gameEnded = true;
            showMenu();
        } else if (data.status === "draw") {
            alert("It's a draw!");
            gameEnded = true;
            showMenu();
        }
    }, 100); // Slight delay (100 ms)
}

function resetGame() {
    gameEnded = false;  // Reset the game state
    showMenu();
}

function startGame(mode) {
    gameMode = mode;
    fetch("/reset", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mode }),
    }).then(() => {
        document.getElementById("menu").style.display = "none";
        document.getElementById("game").style.display = "block";
        createBoard();
        currentPlayer = "X";  // Reset to player X for a new game
        document.getElementById("turn-indicator").textContent = `Player ${currentPlayer}'s turn`;
        gameEnded = false;  // Reset game ended state when starting a new game
    });
}

function updateBoard(board) {
    const cells = document.querySelectorAll("#board div");
    cells.forEach(cell => {
        const x = cell.dataset.x;
        const y = cell.dataset.y;
        cell.textContent = board[x][y];
        cell.style.pointerEvents = board[x][y] ? "none" : "auto";
    });
}

function highlightWinningCells(winningCells) {
    const cells = document.querySelectorAll("#board div");
    winningCells.forEach(([x, y]) => {
        const winningCell = Array.from(cells).find(cell => {
            return parseInt(cell.dataset.x) === x && parseInt(cell.dataset.y) === y;
        });
        if (winningCell) {
            winningCell.style.backgroundColor = "green";  // Highlight the winning cell
        }
    });
}

function showMenu() {
    document.getElementById("game").style.display = "none";
    document.getElementById("menu").style.display = "flex";
}

document.addEventListener("DOMContentLoaded", () => {
    showMenu();
});
