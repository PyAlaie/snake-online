import socket, threading, time, pickle, struct
from getkey import getkey, keys

HOST = "127.0.0.1"  
PORT = 3141

def print_map(snake_map, *args, **kwargs):
        for i in snake_map:
            for j in i:
                print(j, end='')
            print()
        print(args, kwargs)  

class Input_stream():
    def __init__(self, input_stream):
        self.input_stream = input_stream
    
    def run_stream(self):
        print("Input stream stablish!")
        while(1):
            size_in_4_bytes = self.input_stream.recv(4)
            size = struct.unpack('I', size_in_4_bytes)[0]

            data = self.input_stream.recv(size)
            if not data:
                continue
            
            snake_map = pickle.loads(data)
            print_map(snake_map)
            
    
class Output_stream():
    def __init__(self, output_stream):
        self.output_stream = output_stream
    
    def run_stream(self):
        print("Output stream stablish!")
        while 1:
            key = getkey()
            self.output_stream.send(key.encode())
        
    def read_key(self):
        key = getkey()
        return key

# Connecting to the sockets
input_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
input_socket.connect((HOST, PORT))
input_stream = Input_stream(input_socket)

time.sleep(1)
output_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
output_socket.connect((HOST, 3142))
output_socket.setblocking(True)
output_stream = Output_stream(output_socket)

# Starting the threads
input_thread = threading.Thread(target=input_stream.run_stream)
output_thread = threading.Thread(target=output_stream.run_stream)
input_thread.start()
output_thread.start()