from socket import *    

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789

serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
	print('Waiting for client request...')
	connectionSocket, addr = serverSocket.accept()
	
	try:
		message =  connectionSocket.recv(1024)
		print(message)
		filename = message.split()[1]
		print(filename)
		f = open(filename[1:])
		outputdata = f.read()
		# Send the HTTP response header line to the connection socket
		connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
 
		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i].encode('utf-8'))
		connectionSocket.send(b"\r\n")
		
		connectionSocket.close()

	except IOError:
		connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
		connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")

serverSocket.close()  

