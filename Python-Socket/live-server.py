#!/usr/bin/python
#Server program for accepting client messages
#Michael, 2014

import socket
import sys
 
#Listen on port 5000
HOST = ''
PORT = 5000

Pass = raw_input('KEY: ')

#Create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind to socket unless error
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'STATUS: Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
s.listen(10)
print 'STATUS: Server is running.'

#Keep listener running and respond to incoming packet
while 1:
    conn, addr = s.accept()
    print 'STATUS: Incoming connection from ' + addr[0] + ':' + str(addr[1])
    data = conn.recv(1024)

	encodedPass = hashlib.sha256(Pass).digest()

	length = 16 - (len(data) % 16)
	data += chr(length)*length

	#Decrypt function
	DecryptData = AES.new(encodedPass, AES.MODE_ECB)
plaintext = DecryptData.decrypt(base64.b64decode(data))
print plaintext
reply = 'Recieved.' 

conn.sendall(reply)
 
#Close connection and close socket
conn.close()
s.close()
