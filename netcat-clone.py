import socket
import sys 
import threading 
import subprocess
import shlex 
import argparse
import textwrap

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Net Tools', formatter_class=argparse.RawDescriptionHelpFormatter, 
    epilog=textwrap.dedent(
        '''
        netcat.py -t 00.00.00.00 -p 0000 -l -c #command shell
        netcat.py -t 00.00.00.00 -p 0000 -l -u=test.txt #upload to file
        netcat.py -t 00.00.00.00 -p -e="cat /etc/passwd" # execute command 
        echo 'ABC' | ./netcat.py -t 00.00.00.00 -p 123 # echo text to server port 123
        netcat.py -t 00.00.00.00 -p 0000 # connect to server
        '''


    ))
    '''
    - '-c' setup interactive shell
    - '-e' executes one specific command
    - '-h' indicates that a listner should be setup
    - '-p' specifies the port on which to communicate
    - '-t' specifies the target IP
    - '-u' specifies the name of file to upload
    - the '-c' , '-e' and '-u' args imply the '-l' argument because those args apply to only listener side of communication
    - the sender side makes the connection to listener so it needs only the '-t' and '-p' args to define the target listener
    '''

parser.add_argument('-c', '--command', action = 'store_true', help = 'command shell')
parser.add_argument('-e', '--execute', help = 'execute specfied command')
parser.add_argument('-l', '--listen', action = 'store_true', help = 'listen')
parser.add_argument('-p', '--port', type=int, default=5555, help='specified port') 
parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP') 
parser.add_argument('-u', '--upload', help='upload file') 

args = parser.parse_args()

if args.listen:
    buffer = ''
else:
    buffer = sys.stdin.read()

nc = Netcat(args , buffer.encode()) 
nc.run()

class Netcat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()
    def send(self):
        def listen(self):
            def handle(self, client_socket):
               #handle method
               
               
             def send(self):
                        self.socket.connect((self.args.target, self.args.port))
                        if self.buffer:
                            self.socket.send(self.buffer)
                        else:
                            try:
                                while True:
                                    recive_len = 1
                                    response = ''
                                    data = self.socket.recv(4096)
                                    recive_len = len(data)
                                    response += data
                                    
                                    if(recive_len < 4096):
                                        break
                                    if response:
                                        print(f'{response}')
                                        buffer = input('> ')
                                        buffer += '\n'
                                    self.socket.send(buffer.encode())

                            except KeyboardInterrupt:
                                print("[-] User terminated")
                                self.socket.close()
                                sys.exit()

def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)

        while True:
            try:
                client_socket, _ = self.socket.accept()
                client_thread = threading.Thread(target=self.handle, args=(client_socket,))
                client_thread.start()
            except Exception as e:
                print(f"[-] server killed {e}") 
                self.socket.close()
                sys.exit()      

               

def handle(self, client_socket):
                    if self.args.execute:
                        try:
                            output = execute(self.args.execute)
                            client_socket.send(output.encode())
                        except:
                            print("[-] Something went worong")

                    elif self.args.upload:
                        file_buffer = b''
                        while True:
                            data = client_socket.recv(4096)
                            if data:
                                file_buffer += data
                            else:
                                break
                        with open(self.args.upload, 'wb') as f:
                            f.write(file_buffer)

                        message = f"[+] File Saved {self.args.upload}"
                        client_socket.send(message.encode())

                    elif self.args.commad:
                        cnd_buffer = b''
                        while True:
                            try:
                                client_socket.send(b'CMD: #>')
                                while '\n' not in cmd_buffer.decode():
                                    #get the commands from client
                                    cmd_buffer += client_socket.recv(64)
                                    response = execute(cmd_buffer.decode())
                                    if response:
                                        #send the response to the client
                                        client_socket.send(response.encode())
                                        cmd_buffer = b''
                                    else:
                                        client_socket.send("[-] Something went wrong")
                                        self.socket.send()
                                        sys.exit()
                            except Exception as e:
                                #if something went wtong
                                print(f'[-] server killed {e}')
                                self.scoket.close()
                                sys.exit()
