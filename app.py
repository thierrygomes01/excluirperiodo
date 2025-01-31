import sys
import codecs
from imap_tools import MailBox, A
from datetime import datetime, date

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach(), errors='replace')

# Dados para conexão
username = "seu_email@gmail.com" #Digite seu email
senha = "sua_senha_de_app" #Digite sua senha

# Indicar o periodo de exclusão
data_inicio = datetime(2020, 1, 1).date()  #  Data Inicio
data_fim = datetime(2022, 12, 31).date()     # Data Fim

# Conecta ao servidor IMAP
with MailBox("imap.gmail.com").login(username, senha, 'INBOX') as meu_email:
    # Busca os e-mails dentro do período especificado
    emails_para_excluir = meu_email.fetch(A(date_gte=data_inicio, date_lt=data_fim))

    contador = 0  # Inicia a Contagem
    for email in emails_para_excluir:
        contador += 1  # Incrementa o contador
        print(f"Excluindo {contador}: {email.subject} de {email.date}")
        # Excluir o e-mail
        meu_email.delete(email.uid)

    print("Processo de exclusão concluído.")