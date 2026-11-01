import socket
import threading

port = 5000
format = "utf-8"
buffer = 16
disconnected = "End"

hostname = socket.gethostname()
host_ip_address = socket.gethostbyname(hostname)

server_socket_address = (host_ip_address, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)
server.listen()
print(f"Server is Listening on {host_ip_address}:{port}")


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True

    while connected:
        try:
            message_length = conn.recv(buffer).decode(format)
            
            if message_length:
                message_length = int(message_length)
                msg = conn.recv(message_length).decode(format)
                
                if msg == disconnected:
                    conn.send("Goodbye. It was nice to serve you.".encode(format))
                    print(f"[{addr}] Terminating connection.")
                    connected = False
                    break 
                else:
                    print(f"[{addr}] Hours worked received: {msg}")
                    
                    try:
                        hours = float(msg)
                        if hours <= 40:
                            salary = hours * 200
                        else:
                            salary = 8000 + ((hours - 40) * 300)
                            
                        response = f"Calculated Salary: Tk {salary}"
                    except ValueError:
                        response = "Error: Please send a valid numeric value for hours."

                    conn.send(response.encode(format))
        except ConnectionResetError:
            break

    conn.close()

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")