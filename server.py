import socket

def main():
    host = 'localhost'
    port = 5000
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Servidor ouvindo em {host}:{port}')

    while True:
        conn, addr = server_socket.accept()
        print(f'Conexão de {addr}')
        data = conn.recv(1024).decode()
        if not data:
            break
        try:
            base, height = map(float, data.split(','))
            area = (base * height) / 2
            conn.send(str(area).encode())
        except Exception as e:
            conn.send(f'Erro: {e}'.encode())
        conn.close()

if __name__ == '__main__':
    main()
