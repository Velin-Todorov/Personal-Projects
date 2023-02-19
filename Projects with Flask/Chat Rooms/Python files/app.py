import asyncio
import websockets
import json
from connect4 import PLAYER1, PLAYER2, Connect4


async def handler(websocket):
    game = Connect4()
    current_player = PLAYER1

    async for message in websocket:
        print(current_player)
        print(message)
        parsed_message = json.loads(message)
        column = parsed_message['column']

        try:
            row = game.play(current_player, int(column))

            event = {
                'type': 'play',
                'player': current_player,
                'column': column,
                'row': row
            }
            await websocket.send(json.dumps(event))

        except RuntimeError as e:
            print(e)
            print('Runtime Error happened')
            event = {
                'type': 'error'
            }
            await websocket.send(json.dumps(event))

        if game.last_player_won:
            event = {
                'type': 'win',
                'player': current_player
            }
            await websocket.send(json.dumps(event))

        if current_player == PLAYER1:
            current_player = PLAYER2
        else:
            current_player = PLAYER1


async def main():
    """This is a coroutine that starts a websocket server."""
    async with websockets.serve(handler, '', 8001):
        # handler - a coroutine that manages the connection when a client connects or closes the connection.
        # '' - defines the network interface the network interfaces where the server can be reached. We listen on all interfaces, so that devices on the same local network can connect
        # 8001 defines the port
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())
