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
                    print(f"[{addr}] {msg}")
                    
                vowels = "aeiouAEIOU"
                total = 0
                for i in msg:
                    if i in vowels:
                        total += 1

                if total == 0:
                    conn.send("Not enough vowels".encode(format))
                elif total <= 2:
                    conn.send("Enough vowels I guess".encode(format))
                else:
                    conn.send("Too many vowels".encode(format))
        except ConnectionResetError:
            break

    conn.close()

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")