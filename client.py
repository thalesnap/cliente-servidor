import socket

def main():
    host = 'localhost'
    port = 5000
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    base = input('Digite a base do triângulo: ')
    height = input('Digite a altura do triângulo: ')
    
    client_socket.send(f'{base},{height}'.encode())
    area = client_socket.recv(1024).decode()
    print('A área do triângulo é:', area)
    client_socket.close()

if __name__ == '__main__':
    main()
