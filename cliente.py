import threading
import socket
import tkinter as tk
from tkinter import scrolledtext, END

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect(('localhost', 7777))  # Troque 'localhost' pelo IP do servidor
    except Exception as e:
        return print(f"\nNão foi possível se conectar ao servidor! Erro: {e}\n")
    
    usuario = ''  # Variável de usuário

    def salvar_usuario():
        nonlocal usuario  # Usar 'nonlocal' para modificar a variável do escopo externo
        usuario = entry_input.get().strip()
        if usuario:  
            root.destroy()
            abrir_janela_chat()

    def abrir_janela_chat():
        chat_window = tk.Tk()
        chat_window.title("Chat")
        
        # Dimensões da janela de chat
        largura_janela = 720
        altura_janela = 520
        largura_tela = chat_window.winfo_screenwidth()
        altura_tela = chat_window.winfo_screenheight()

        # Cálculo para centralizar
        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2

        # Define a posição e tamanho da janela de chat
        chat_window.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

        # Área de texto para exibir mensagens
        text_area = scrolledtext.ScrolledText(chat_window, wrap=tk.WORD, state='disabled')
        text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Função para enviar mensagem
        def enviar_mensagem_gui():
            mensagem = entry_message.get().strip()
            if mensagem:
                try:
                    cliente.send(f'[{usuario}]: {mensagem}'.encode('utf-8'))
                    text_area.config(state='normal')
                    text_area.insert(END, f'[{usuario}]: {mensagem}\n')
                    text_area.config(state='disabled')
                    entry_message.delete(0, END)
                except Exception as e:
                    text_area.config(state='normal')
                    text_area.insert(END, f'Erro ao enviar a mensagem: {e}\n')
                    text_area.config(state='disabled')

        # Caixa de entrada para novas mensagens
        entry_message = tk.Entry(chat_window, width=50)
        entry_message.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
        entry_message.bind("<Return>", lambda event: enviar_mensagem_gui())  # Permite enviar ao pressionar Enter

        # Botão de enviar mensagem
        button_send = tk.Button(chat_window, text="Enviar", command=enviar_mensagem_gui)
        button_send.pack(side=tk.RIGHT, padx=10, pady=10)

        # Thread para receber mensagens
        thread_receber = threading.Thread(target=receberMensagem, args=[cliente, text_area])
        thread_receber.start()

        chat_window.mainloop()

    root = tk.Tk()
    root.title("Chatbox")
    
    # Dimensões da janela principal
    largura_janela = 400
    altura_janela = 300
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Cálculo para centralizar
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2

    # Define a posição e tamanho da janela principal
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    label = tk.Label(root, text="Digite seu nome:")
    label.pack(pady=10)

    entry_input = tk.Entry(root, width=40)
    entry_input.pack(pady=10)

    button_salvar = tk.Button(root, text="Salvar", command=salvar_usuario)
    button_salvar.pack(pady=10)

    root.mainloop()

def receberMensagem(cliente, text_area):
    while True:
        try:
            mensagem = cliente.recv(2048).decode('utf-8')
            if mensagem:
                text_area.config(state='normal')
                text_area.insert(END, mensagem + '\n')
                text_area.yview(END)  # Rolagem automática para a última mensagem
                text_area.config(state='disabled')
        except Exception as e:
            print(f'\nNão foi possível permanecer conectado ao servidor! Erro: {e}\n')
            cliente.close()
            break

main()
