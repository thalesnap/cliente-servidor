# Cliente-Servidor

Este repositório contém uma implementação básica de uma arquitetura cliente-servidor em Python.

## Arquivos

*   `server.py`: Código do servidor. Responsável por receber e processar as requisições dos clientes.
*   `client.py`: Código do cliente. Responsável por se conectar ao servidor e enviar requisições.

## Como executar

1.  Primeiro, execute o servidor:
    ```bash
    python server.py
2. Em seguida, em outro terminal, execute o cliente:
   ```bash
    python client.py
3. O cliente enviará uma mensagem para o servidor e aguardará a resposta.
4. O servidor processará a mensagem e retornará uma resposta ao cliente.
5. A conexão será encerrada após a troca de mensagens.

## Tecnologias utilizadas
- python 3
- Sockets (biblioteca padrão)
