import socket


def run_cliente():
    # Conectamos al servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(( 'localhost', 8000 ))
    print("Conectado al servidor")

    while True:
        # Enviar mensaje al serviddor
        message = input("Mensaje: ")
        server_socket.send(message.encode('utf-8'))

        if message == 'exit':
            break


        # Recibir la respuesta del cliente
        response = server_socket.recv(1024).decode('utf-8')
        print("Servidor: ", response)

    server_socket.close()


if __name__ == "__main__":
    run_cliente()



