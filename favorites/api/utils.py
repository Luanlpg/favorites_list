from email.message import EmailMessage
from smtplib import SMTP
from os import environ

class EmailService:
    """=========================================================================
    Classe de envio de email.
    ========================================================================="""
    def __init__(self):
        self.from_address = 'listfavoritos@gmail.com'
        self.host = 'smtp.gmail.com'
        self.port = 587
        self.password = '123ab123'
        self.server = None

    def __del__(self):
        if self.server:
            self.server.quit()


    def send_token(self, to_address, token):
        """=====================================================================
        Método que envia email com token de autenticação para usuário.
        ====================================================================="""
        if not self.server:
            self._start_server()

        message = EmailMessage()
        message['From'] = self.from_address
        message['To'] = to_address
        message['Subject'] = '[Favorites list] - Bem vindo! Aqui está seu token'
        message_content =   f'Seja bem vindo ao Favorites list!\n\n'\
                            f'Aqui está seu token de autenticação: {token}\n\n'\
                            f'Ele será necessário em todos os endpoints da API.'
        message.set_content(message_content)

        self.server.send_message(message)

    def _start_server(self):
        self.server = SMTP(host=self.host, port=self.port)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(self.from_address, self.password)
