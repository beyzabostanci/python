#networked programs
#TCP -built on top of IP, assumes IP might lose some data-stores and retransmits data if it seems to be lost, handles "flow control" using a transmit window, provides a nice reliable pipe(connection)
# data phonecall-an internet socket or network socket is an endpoint of a bidirectional inter-process communication flow across an internet protocol-based computer network, such as the internet--process<internet>process
#TCP Port Numbers
#Common TCP Ports
#Telnet(23)-Login
#SSH(22)-Secure Login
#HTTP(80)
#HTTPS(443)-Secure
#SMTP(25) (mail)
#IMAP(143/220/993)-Mail Retrieval
#POP(109/110)-Mail Retrival
#DNS(53)-Domain Name
#FTP(21)-File Transfer

#SOCKETS IN PYTHON
#import socket
#valuename  = created value
#valuename.connect()

#APPLICATION PROTOCOL-what are we gonna send what are we gonna expect
#mail
#www

#HTTP protocol

#protocol is rules that all parties follow

#http://  www.xxx.com /page.htm
#protocol   host      document

#INTERNET STANDARTS
#w3schools has protocols


#What type of HTTP request is usually used to access a website?
#GET

#.encode()
#.send()

#import socket

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#mysock.send(cmd)

#while True:
#    data = mysock.recv(512)
#    if len(data) < 1:
#        break
#    print(data.decode(),end='')
#mysock.close()

#creates simple web browser


#TEXT PROCESSING

#ASCII character set

#ord()
print(ord("H"))

#UTF-8>>1-4 bytes, dynamic length
#UTF-32   UTF-16


#bytes.decode()
#bytearray.decode()
#recv()
# encode()
# decode()-makes bytes string




#USING URLLIB IN PYTHON

#you can read a webpage with it
#you can open links with loops

#import urllib.request #library
#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#for line in fhand:
#    print(line.decode().strip())

#urlopen()
#strip()




#HTML PARSING-web scraping with python

#beautifulsoup4 www.crummy.com
#bs4.zip file

#read()
#get()

#excersizes
