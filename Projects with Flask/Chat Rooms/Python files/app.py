import asyncio
import websockets
import json
from connect4 import PLAYER1, PLAYER2, Connect4
import logging
import itertools
import secrets


#logging.basicConfig(format="%(message)s", level=logging.DEBUG)

JOIN = {}
# async def handler(websocket):
#     game = Connect4()
#     turns = itertools.cycle([PLAYER1, PLAYER2])
#     current_player = next(turns)

#     async for message in websocket:

#         parsed_message = json.loads(message)
#         column = parsed_message['column']

#         try:
#             row = game.play(current_player, int(column))

#             event = {
#                 'type': 'play',
#                 'player': current_player,
#                 'column': column,
#                 'row': row
#             }
#             await websocket.send(json.dumps(event))

#         except RuntimeError as e:
#             print(e)
#             print('Runtime Error happened')
#             event = {
#                 'type': 'error'
#             }
#             await websocket.send(json.dumps(event))

#         if game.winner is not None:
#             event = {
#                 'type': 'win',
#                 'player': current_player
#             }
#             await websocket.send(json.dumps(event))

#         current_player = next(turns)

async def error(websocket, message):
    event = {
        'type': 'error',
        'message': message
    }

    await websocket.send(json.dumps(message))

async def join(websocket, join_key):
    print('Entered join()')
    try:
        game, connected = JOIN[join_key]
        print(JOIN)

    except KeyError:
        await error(websocket, "Game not found")
        return 

    connected.add(websocket)
    try:
        print('second player joined the game', id(game))

        async for message in websocket:
            print('second player sent', message)
    
    finally:
        connected.remove(websocket)

async def start(websocket):
    game = Connect4()
    connected = {websocket}

    join_key = secrets.token_urlsafe(12)
    
    JOIN[join_key] = game, connected

    try:

        event = {
            'type': 'init',
            'join': join_key
        }

        await websocket.send(json.dumps(event))

        print("first player started game", id(game))

        async for message in websocket:
            print("first player sent", message)
    finally:
        del JOIN[join_key]

async def handler(websocket):
    message = await websocket.recv()
    event = json.loads(message)
    assert event['type'] == 'init'

    if 'join' in event:
        print('I am here')
        print(event)
        await join(websocket, event['join'])

    else:
        await start(websocket)


async def main():
    """This is a coroutine that starts a websocket server."""
    async with websockets.serve(handler, '', 8001):
        # handler - a coroutine that manages the connection when a client connects or closes the connection.
        # '' - defines the network interface the network interfaces where the server can be reached. We listen on all interfaces, so that devices on the same local network can connect
        # 8001 defines the port
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())
