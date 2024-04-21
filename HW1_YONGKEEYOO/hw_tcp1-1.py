import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

name = "Yongkee Yoo"
sock.sendall(name.encode())

student_number_raw = sock.recv(4)
student_number = struct.unpack('I', student_number_raw)[0]
print("Received student number:", student_number)

sock.close()
