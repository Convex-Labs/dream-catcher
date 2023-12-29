from aineko.core.node import AbstractNode
import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from sqlalchemy import create_engine

# Define your Gmail Fetcher Node
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
        for msg in messages:
            # Get the message detail
            txt = self.service.users().messages().get(userId='me', id=msg['id']).execute()
            try:
                # Decode the email body
                payload = txt['payload']
                headers = payload['headers']
                parts = payload.get('parts')[0]
                data = parts['body']['data']
                data = data.replace("-", "+").replace("_", "/")
                decoded_data = base64.b64decode(data)
                # Emit the email content
                self.producers['email_content'].produce(decoded_data)
            except Exception as e:
                self.log(f'Failed to fetch email: {e}', level='error')

# Define your Database Writer Node
class DatabaseWriter(AbstractNode):
    def _pre_loop_hook(self, params=None):
        # Initialize database connection
        self.engine = create_engine(params['database_url'])

    def _execute(self, params=None):
        # Write email content to the database
        email_content = self.consumers['email_content'].next()
        if email_content:
            # Here you would write the email content to your database
            # For example, using SQLAlchemy to insert into a table
            with self.engine.connect() as connection:
                connection.execute("INSERT INTO emails (content) VALUES (:content)", {'content': email_content})