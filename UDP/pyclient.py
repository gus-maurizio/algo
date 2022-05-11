import socket, sys, time

ip = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
port = int(sys.argv[2]) if len(sys.argv) > 2 else 30000
reqs = int(sys.argv[3]) if len(sys.argv) > 3 else 5
tout = float(sys.argv[4]) if len(sys.argv) > 4 else 1.5

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.settimeout(tout)
print("Do Ctrl+c to exit the program !!")

# Let's send data through UDP protocol
for i in range(reqs):
    send_data = f'Request {i:03d}'
    s.sendto(send_data.encode('utf-8'), (ip, port))
    print(">>> Client Sent :     ", send_data)
    try:
        data, address = s.recvfrom(4096)
    except socket.timeout:
        print(f"Didn't receive data! [Timeout {tout:0.3f}s], retry...")
        continue
    print("           received : ", data.decode('utf-8'))
    time.sleep(1.0)
# close the socket
s.close()
