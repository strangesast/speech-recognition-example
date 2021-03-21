import os
import sys
import asyncio
import websockets


async def hello(uri, fname):
    async with websockets.connect(uri) as websocket:
        with open(fname, "rb") as wf:
            while True:
                data = wf.read(1000000)
                #data = wf.read(100000)

                if len(data) == 0:
                    break

                await websocket.send(data)
                print (await websocket.recv())

            await websocket.send('{"eof" : 1}')
            print (await websocket.recv())


if __name__ == '__main__':
    HOST = os.environ.get('HOST', 'localhost')
    PORT = int(os.environ.get('PORT', '2700'))
    asyncio.run(hello(f'ws://{HOST}:{PORT}', 'audio.wav'))
