# Script de Exclusão de E-mails

Este script Python permite excluir e-mails de uma caixa de entrada do Gmail dentro de um período especificado, utilizando a biblioteca `imap_tools`.

## Pré-requisitos

- Python 3.x instalado.
- Acesso a uma conta do Gmail com permissão para usar aplicativos menos seguros ou com uma senha de app gerada.

## Instalação

1. Clone este repositório ou faça o download do script.

2. Instale a biblioteca `imap_tools` utilizando o pip:

   ```bash
   pip install imap-tools
   ```

Configuração
Abra o arquivo script.py e substitua os seguintes valores:

username: Substitua "seu_email@gmail.com" pelo seu endereço de e-mail do Gmail.

senha: Substitua "sua_senha_de_app" pela sua senha de app do Gmail.

Defina o período de exclusão ajustando as variáveis data_inicio e data_fim no script.

Exemplo:

    ```python
    data_inicio = datetime(2020, 1, 1).date()  # Data de início
    data_fim = datetime(2022, 12, 31).date()   # Data de fim
    ```

Execução
Execute o script utilizando o Python:

    ```bash
    python script.py
    ```

Funcionamento
O script se conecta à caixa de entrada do Gmail usando o protocolo IMAP.

Ele busca e exclui e-mails recebidos dentro do período especificado.

O progresso da exclusão é exibido no terminal.

Aviso
Este script exclui permanentemente os e-mails. Certifique-se de que você realmente deseja excluir os e-mails antes de executar o script.

Recomenda-se fazer um backup dos e-mails importantes antes de prosseguir.