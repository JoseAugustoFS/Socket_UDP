import socket
import sys

#endereço para o qual os dados vão ser enviados
host = 'localhost'

#número da porta que o servidor que vai receber os dados está escutando
port = 1234

#cria um UDP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Para sair use CTRL+X e pressione enter\n')
msg = input("Digite a mensagem: ")

while msg != '\x18':
	#envia os dados
	s.sendto(msg.encode(), (host, port))
	
	msg = input("Digite a mensagem: ")
	
print('closing socket')
s.close()

#fonte: http://www2.ic.uff.br/~debora/praticas/aplicacao/