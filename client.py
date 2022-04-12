import socket
import time
from random import randint

test_socket_ip = ('127.0.0.1', 55556)

# connect to rendezvous

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#sock.bind(('127.0.0.1', 55557))
while True:
    sock.sendto(str(randint(1, 10)).encode(), test_socket_ip)
    print(sock.recvfrom(1024))
    time.sleep(1)

#sock.close()
