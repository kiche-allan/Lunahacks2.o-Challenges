const cells = document.querySelectorAll('[data-cell]');
const status = document.querySelector('.status');
const restartBtn = document.querySelector('.restart-btn');

let currentPlayer = 'X';
let gameActive = true;
let gameState = ['', '', '', '', '', '', '', '', ''];

const winningMessage = () => `Player ${currentPlayer} has won!`;
const drawMessage = () => `Game ended in a draw!`;
const currentPlayerTurn = () => `Player ${currentPlayer}'s turn`;

status.innerHTML = currentPlayerTurn();

const handleCellClick = (e) => {
  const cell = e.target;
  const cellIndex = Array.from(cells).indexOf(cell);
  if (gameState[cellIndex] !== '' || !gameActive) return;
  gameState[cellIndex] = currentPlayer;
  cell.innerHTML = currentPlayer;
  handleResultValidation();
};

const handleResultValidation = () => {
  const winningCombinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
   
  ]};