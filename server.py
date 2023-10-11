import socket
import threading
from server_connection import Client
from game import Game
from snake import Snake
from coordinates import Coordinates

coords = [Coordinates(5,4), Coordinates(5,5)]

# Initializing socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 3141))
serverSocket.listen(4)
print("Server started on port 3141 ...")
print("Listening for Connections ...")

clients = []
while True:
    # Listening for connections
    clientSocketOutputStream, address = serverSocket.accept()
    print("New Connection:", clientSocketOutputStream.getpeername()[1])
    snake = Snake(coords)
    client = Client(clientSocketOutputStream, snake)
    thread = threading.Thread(target=client.runClient)
    thread.start()
    clients.append(client)
    
    # if all 4 players have joined stop accepting new connections
    if len(clients) == 1:
        print("All players joined!")
        break


# Initializing game
game = Game(clients)