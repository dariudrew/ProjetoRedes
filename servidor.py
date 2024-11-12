import threading
import socket
import tkinter as tk
from tkinter import PhotoImage, messagebox

clientes = []
servidor = None
servidor_ativo = False  

def iniciar_servidor():
    global servidor, servidor_ativo
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        servidor.bind(('localhost', 7777)) 
        servidor.listen()
        servidor_ativo = True
        atualizar_mensagem("Servidor ativo")
        print('Servidor iniciado e aguardando conexões...')
        
        while servidor_ativo:
            cliente, endereco = servidor.accept()
            clientes.append(cliente)
            print(f"Nova conexão de {endereco}")
            thread = threading.Thread(target=tratando_mensagens, args=[cliente])
            thread.start()
    except Exception as e:
        if servidor_ativo:
            atualizar_mensagem("Servidor desligado")
            messagebox.showerror("Erro", f"Não foi possível iniciar o servidor. Erro: {e}")

def parar_servidor():
    global servidor, servidor_ativo
    servidor_ativo = False
    atualizar_mensagem("Servidor desligado")
    if servidor:
        servidor.close()
        servidor = None
        for cliente in clientes:
            cliente.close()
        clientes.clear()
    print("Servidor parado")

def tratando_mensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(2048)
            if mensagem:
                broadcast(cliente, mensagem)
            else:
                excluir_cliente(cliente)
                break
        except:
            excluir_cliente(cliente)
            break

def broadcast(cliente, mensagem):
    for usuario in clientes:
        if usuario != cliente:
            try:
                usuario.send(mensagem)
            except:
                excluir_cliente(usuario)

def excluir_cliente(cliente):
    if cliente in clientes:
        clientes.remove(cliente)
        cliente.close()
        print(f"Conexão com cliente {cliente} encerrada.")

def atualizar_mensagem(texto):
    if texto == "Servidor ativo":
        label_status.config(text=texto, fg="#019d00")
    else:
        label_status.config(text=texto, fg="#cb0000")
        

def iniciar_interface():
    global janela, label_status, label_imagem

    janela = tk.Tk()
    janela.title("Servidor de Conexão")
    janela.resizable(False, False)
    janela.geometry(f"450x300+400+200")

    try:
        imagem = PhotoImage(file='globo.png').subsample(11,11)
        label_imagem = tk.Label(janela, image=imagem)
        label_imagem.image = imagem  
        label_imagem.pack(pady=(5,0))  
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")

    label_status = tk.Label(janela, text="Servidor desligado", font=("Arial", 24), fg="#cb0000")
    label_status.pack(pady=0)

    button_ligar = tk.Button(janela, text="Ligar Servidor", font=("Georgia", 12), bg="#706f6e", fg="white", command=lambda: threading.Thread(target=iniciar_servidor).start())
    button_ligar.pack(side=tk.LEFT, ipadx=15, ipady=8, padx=20, pady=20, expand=True)

    button_desligar = tk.Button(janela, text="Desligar Servidor", font=("Georgia", 12), bg="#706f6e", fg="white", command=parar_servidor)
    button_desligar.pack(side=tk.RIGHT, ipadx=5, ipady=8, padx=20, pady=20, expand=True)

    janela.mainloop()

iniciar_interface()
