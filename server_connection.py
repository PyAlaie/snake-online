import socket
import threading, pickle, struct

class Input_stream():
    def __init__(self, snake, input_stream) -> None:
        self.snake = snake
        self.input_stream = input_stream
        
    def runClient(self):
        while(1):
            data = self.input_stream.recv(1024)
            data = data.decode('utf-8')
            self.snake.change_direction(data)
        
class Output_stream():
    def __init__(self, snake, output_stream) -> None:
        self.snake = snake
        self.input_stream = output_stream
        
    def runClient(self):
        pass

class Client():
    def __init__(self, socket_connection, snake):
        self.output_stream = socket_connection
        self.input_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.input_stream = None
        self.snake = snake
        print("init client")
        
        
    
    def runClient(self):
        try:
            # Initializing input stream
            self.input_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.input_socket.bind(("127.0.0.1", 3142))
            self.input_socket.listen(4)
            self.input_stream, address = self.input_socket.accept()
            
            input_stream_thread = Input_stream(self.snake, self.input_stream)
            
            thread = threading.Thread(target=input_stream_thread.runClient)
            thread.start()
        except KeyboardInterrupt:
            self.input_socket.close()
        
    def send_map_to_client(self, snake_map):
        data = pickle.dumps(snake_map)
        
        size = len(data)
        size_in_4_bytes = struct.pack('I', size)
        self.output_stream.send(size_in_4_bytes)
        
        self.output_stream.send(data)