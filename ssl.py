#A python program to illustrate SSL Algorithm.

import socket
import ssl

print("\n#A python program to Implement SSL Algorithm.\n")

Technique = 'SSL'

ctx = ssl.create_default_context()
ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
ctx.verify_mode = ssl.CERT_REQUIRED
ctx.check_hostname = True
ctx.load_default_certs()

website = input("\nEnter the WebSite You want to get Connect...\n\n")
server_host = input("\nEnter The Website's Server_hostname...\n\n")
server_port_send = int(input("\nEnter The Port Number You want to use To Send \n[To use By Default use '443']...\n\n"))
server_port_receive = int(input("\nEnter The Port Number You want to use To Receive \n[To use By Default use '1024']...\n\n"))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ctx.wrap_socket(socket.socket(socket.AF_INET), server_hostname = server_host)
ssl_sock.connect((website, server_port_send))
cert = ssl_sock.getpeercert()
#print(cert)
ssl_sock.sendall(b"HEAD / HTTP/1.0\r\nHost: linuxfr.org\r\n\r\n")
Receive = (ssl_sock.recv(server_port_receive).split(b"\r\n"))


print ("\nYour Mode      : " + Technique)
print ("\nYour Website   : " + website)
print ("\nSending Port   : " + str(server_port_send))
print ("\nReceiving Port : " + str(server_port_receive))
print ("\nPeering Cert   : \n\n" + str(cert))
print ("\nResponse       : \n\n" + str(Receive))
