import os,socket,sys

adresse_hote = ''
numero_port = 6800
tsap_relais = ('',6789)
ma_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM,socket.IPPROTO_TCP)
ma_socket.bind(adresse_hote,numero_port)

while 1:
    (nouvelle_connexion,depuis) = ma_socket.accept()
    pid = os.fork()
    if (not pid):
        socket_relais = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_relais.connect(tsap_relais)
        pid2 = os.fork
        if pid2:
            while 1:
                donnes = ma_socket.recv(1024)
                socket_relais.send(donnes)
            nouvelle_connexion.close()
            socket_relais.close()
            sys.exit(0)
        else:
            while 1:
                donnes = socket_relais.recv(1024)
                ma_socket.sendall(donnes)
            nouvelle_connexion.close()
            socket_relais.close()
            sys.exit()
ma_socket.close()