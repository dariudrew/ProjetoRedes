import threading
import socket

clientes = []

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        servidor.bind(('localhost', 7777))
        servidor.listen()
    except:
        return print('\nNão foi possivel se conectar ao servidor!\n')
    
    while True:
        cliente, endereco = servidor.accept()
        clientes.append(cliente)

       
        thread = threading.Thread(target=tratandoMensagens, args=[cliente])
        thread.start()


def tratandoMensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(2048)
            broadcast(cliente, mensagem)
        except:
            excluirCliente(cliente)
            break

def broadcast(cliente, mensagem):
    for usuario in clientes:
        if usuario != cliente:
            try:
                usuario.send(mensagem)
            except:
                excluirCliente(usuario)

def excluirCliente(cliente):
    clientes.remove(cliente)

main()