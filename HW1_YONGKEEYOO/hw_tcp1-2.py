import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from', addr)
    
    client.send(b'Hello ' + addr[0].encode())
    
    student_name = client.recv(1024).decode()
    print("Student's name:", student_name)
    
    student_number = 20191513
    student_number_raw = struct.pack('I', student_number)
    client.sendall(student_number_raw)
    
    client.close()
