import socket, sys
from ordereduuid import OrderedUUID

ip = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
port = int(sys.argv[2]) if len(sys.argv) > 2 else 30000

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (ip, port)
s.bind(server_address)
print("Do Ctrl+c to exit the program !!")

while True:
    print("####### Server is listening #######")
    data, address = s.recvfrom(4096)
    print("Server received: ", data.decode('utf-8'), f' from {address}')
    answer  = OrderedUUID()
    ansInt  = answer.int
    ansByte = answer.int.to_bytes(16, 'big')
    send_data = f'{answer},{ansInt},{repr(ansByte)},{len(ansByte)}'
    s.sendto(send_data.encode('utf-8'), address)
    print("       sent :    ", send_data)
