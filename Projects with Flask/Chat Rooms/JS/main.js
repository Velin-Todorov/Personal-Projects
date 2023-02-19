import { createBoard, playMove } from "./connect4.js"; 

window.addEventListener('DOMContentLoaded', () => {
    const board = document.querySelector('.board');
    createBoard(board)
})