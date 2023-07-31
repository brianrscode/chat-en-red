import socket
import threading


def handle_client(cliente_socket, cliente_address):
    while True:
        try:
            # Recibir datos del cliente
            data = cliente_socket.recv(1024).decode('utf-8')
            print(f"Cliente {cliente_address}: {data}")

            if data == "exit":
                break

            # Enviar respuesta al cliente
            response = input("Restpuesta: ")
            cliente_socket.send(response.encode('utf-8'))

        except Exception as e:
            raise e

    # Cerrar la conexión
    cliente_socket.close()


def run_server():
    # configurar el servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(5)
    print("Servidor iniciado. Esperando conexiones...")
    while True:
        cliente_socket, cliente_address = server_socket.accept()
        print(f"conexión establecida con {cliente_address}")

        # Crear un hilo para manejar el cliente
        cliente_hilo = threading.Thread(target=handle_client, args=(cliente_socket, cliente_address))
        cliente_hilo.start()


if __name__ == "__main__":
    run_server()
