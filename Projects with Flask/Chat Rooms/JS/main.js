import { createBoard, playMove } from "./connect4.js";

window.addEventListener('DOMContentLoaded', () => {
    const board = document.querySelector('.board');
    createBoard(board)

    const websocket = new WebSocket('ws://localhost:8001/');
    initGame(websocket)
    receiveMoves(board, websocket)
    sendMoves(board, websocket)
})

function sendMoves(board, websocket) {
    board.addEventListener('click', (ev) => {
        const column = ev.target.dataset.column

        if (column == undefined) {
            return;
        }

        const event = {
            type: "play",
            column: parseInt(column, 10)
        };
        websocket.send(JSON.stringify(event))
    })
}

function showMessage(message) {
    window.setTimeout(() => window.alert(message), 50);
}

function receiveMoves(board, websocket) {
    websocket.addEventListener('message', ({ data }) => {
        const event = JSON.parse(data);
        switch (event.type) {
            
            case "init":
                document.querySelector('.join').href = '?join=' + event.join;
                break

            case "play":
                playMove(board, event.player, event.column, event.row);
                break;

            case "win":
                showMessage(`Player ${event.player} wins`);
                websocket.close(1000);
                break;

            case "error":
                showMessage(event.message);
                break;

            default:
                throw new Error(`Unsupported event type: ${event.type}.`);
        }
    });
}

function initGame(websocket) {
    websocket.addEventListener('open', () => {

        const params = new URLSearchParams(window.location.search);
        let event = {
            type: 'init'
        };

        if (params.has('join')) {
            event.join = params.get('join');
        }

        websocket.send(JSON.stringify(event))
    })
}