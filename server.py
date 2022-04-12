import socket

known_port = 50002

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 55556))

while True:
    data, address = sock.recvfrom(128)
    print(data)
    print('connection from: {}'.format(address))

    sock.sendto(b'OK', address)
