import bluetooth
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1

server_sock.bind(("",port))
server_sock.listen(1)

client_sock,address = server_sock.accept()
print "Accepted connection from ", address
while True:
   date = client_sock.recv(1024)
   if (data == "e"):
	print ("Exit")
	break

client_sock.close()
server_sock.close()
