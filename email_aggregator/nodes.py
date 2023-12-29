from aineko.core.node import AbstractNode
import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from sqlalchemy import create_engine
import os

# Define your node classes here

class GmailFetcher(AbstractNode):
    def _pre_loop_hook(self, params=None):
        # Initialize Gmail API
        creds = Credentials(token=params['token'],
                            refresh_token=params['refresh_token'],
                            token_uri=params['token_uri'],
                            client_id=params['client_id'],
                            client_secret=params['client_secret'],
                            scopes=params['scopes'])
        self.service = build('gmail', 'v1', credentials=creds)

    def _execute(self, params=None):
        # Fetch emails from Gmail
        results = self.service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
        messages = results.get('messages', [])
        for message in messages:
            msg = self.service.users().messages().get(userId='me', id=message['id']).execute()
            payload = msg['payload']
            headers = payload.get('headers')
            subject = ''
            for header in headers:
                if header['name'] == 'Subject':
                    subject = header['value']
                    break
            body = payload.get('body').get('data')
            body_decoded = base64.urlsafe_b64decode(body.encode('ASCII'))
            self.producers['email_data'].produce({'subject': subject, 'body': body_decoded})

class DatabaseWriter(AbstractNode):
    def _pre_loop_hook(self, params=None):
        # Initialize database connection
        self.engine = create_engine(params['database_url'])

    def _execute(self, params=None):
        # Write email data to database
        email_data = self.consumers['email_data'].consume()
        if email_data is None:
            return
        with self.engine.connect() as connection:
            connection.execute(
                """INSERT INTO emails (subject, body) VALUES (:subject, :body)""",
                **email_data
            )
