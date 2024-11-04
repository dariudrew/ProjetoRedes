import threading
import socket

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: 
        cliente.connect(('localhost', 7777))
    except:
        return print("\nNão foi possivel se conectar ao servidor!\n")
    usuario = input('Digite seu nome de usuario: ')
    print("\nConectado!")

    threadReceberMensagem = threading.Thread(target=receberMensagem, args=[cliente])
    threadEnviarMensagem = threading.Thread(target=enviarMensagem, args=[cliente, usuario])

    threadEnviarMensagem.start()
    threadReceberMensagem.start()


def receberMensagem(cliente):
    while True:
        try:
            mensagem = cliente.recv(2048).decode('utf-8')
            print(mensagem+'\n')
        except:
            print('\nNão foi possivel permanecer conectado ao servidor!\n')
            print('Pressione <Enter> para continuar...')
            cliente.close()
            break

def enviarMensagem(cliente, usuario):
    while True:
        try:
            mensagem = input('\n')
            cliente.send(f'[{usuario}] : {mensagem}'.encode('utf-8'))
        except:
            return
main()