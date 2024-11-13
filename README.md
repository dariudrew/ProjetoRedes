# Aplicação de Chat Simples em Python

Este projeto é uma aplicação de chat baseada em `socket` e `threading` com interface gráfica usando `tkinter`. O projeto consiste em um servidor de chat que gerencia as conexões dos clientes e um cliente que se conecta ao servidor, permitindo a troca de mensagens em tempo real.

## Pré-requisitos

Para executar este projeto, você precisará do Python instalado na versão 3.x ou superior.

## Estrutura do Projeto

- **Servidor (servidor.py):** código responsável por gerenciar as conexões e distribuir mensagens para todos os clientes conectados.
- **Cliente (cliente.py):** código que executa a interface gráfica para o usuário, permitindo o envio e recebimento de mensagens no chat.


## Como Executar 

Para que a aplicação funcione, é necessário instalar o Tkinter, que é o módulo de interface gráfica do Python. No entanto, se preferir, você pode usar os executáveis já preparados para Windows e Linux nas pastas **Executaveis_Windows** e **Executaveis_Linux**.

### Usando os Executáveis

Se você não quiser instalar o Python ou configurar o ambiente manualmente, você pode usar os executáveis pré-compilados. Siga os passos abaixo:

#### Em Sistemas Windows

1. Navegue até a pasta **Executaveis_Windows**.
2. Execute o arquivo `servidor.exe` para iniciar o servidor.
3. Em outro terminal, execute o arquivo `cliente.exe` para iniciar o cliente.
4. A interface gráfica será aberta, e você pode começar a conversar.

#### Em Sistemas Linux

1. Navegue até a pasta **Executaveis_Linux**.
2. Torne o arquivo executável com o comando:

   ```bash
   chmod +x servidor
   chmod +x cliente
   ```

3. Execute o servidor com:

   ```bash
   ./servidor
   ```

4. Em outro terminal, execute o cliente com:

   ```bash
   ./cliente
   ```

### Instalação do Tkinter

Se você não possui o Tkinter instalado, siga os passos abaixo para instalá-lo.

#### Em Sistemas Linux (Debian/Ubuntu)

Abra o terminal e execute:

```bash
sudo apt-get update
sudo apt-get install python3-tk
```

#### Em Sistemas MacOS

O Tkinter geralmente já está incluído na instalação padrão do Python no MacOS. Caso não esteja, você pode instalá-lo com:

```bash
brew install python-tk
```

#### Em Sistemas Windows

O Tkinter já vem instalado por padrão com o Python no Windows. Se você estiver enfrentando problemas, certifique-se de que o Python está instalado corretamente e que você está utilizando a versão do Python que contém o Tkinter.

---

Agora, com o Tkinter instalado, você pode seguir os passos para rodar o servidor e o cliente.

### Passo 1: Executar o Servidor

1. Abra um terminal e navegue até o diretório do projeto.
2. Execute o servidor com o seguinte comando:

   ```bash
   python3 servidor.py
   ```

   O servidor será iniciado e escutará conexões na porta `7777`. Verifique se esta porta está disponível em sua máquina.

### Passo 2: Executar o Cliente

1. Abra outro terminal e navegue até o mesmo diretório.
2. Execute o cliente com o comando:

   ```bash
   python3 cliente.py
   ```

3. Uma janela será aberta, solicitando que você insira seu nome de usuário. Após inserir, uma nova janela abrirá com o chat.

4. Você pode abrir múltiplas instâncias do cliente em terminais separados para simular múltiplos usuários no chat.

## Possíveis Erros

- **Erro ao Conectar ao Servidor:** Certifique-se de que o servidor está em execução e que o endereço `localhost` e a porta `7777` estão corretos e disponíveis.
- **Erro ao Enviar Mensagem:** Caso o cliente não consiga enviar uma mensagem, verifique a conexão e reinicie o cliente.