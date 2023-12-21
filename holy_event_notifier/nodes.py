from aineko.core.node import AbstractNode
from typing import Optional
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EventMonitorNode(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None):
        self.url = params.get('url')
        self.email_credentials = params.get('email_credentials')
        self.recipients = params.get('recipients')
        self.last_event = None

    def _execute(self, params: Optional[dict] = None):
        try:
            response = requests.get(self.url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                event = self.extract_event(soup)
                if event and event != self.last_event:
                    self.send_email(event)
                    self.last_event = event
        except requests.Timeout:
            self.log('Request to Drik Panchang website timed out.', level='warning')
        except requests.RequestException as e:
            self.log(f'Request to Drik Panchang website failed: {e}', level='error')

    def extract_event(self, soup):
        # This method should be implemented to extract the event details from the Drik Panchang website
        # For example, it might look for a specific tag or class that contains event information
        event_info = soup.find('div', class_='event-class')  # Placeholder for actual HTML parsing logic
        return event_info.text if event_info else None

    def send_email(self, event):
        msg = MIMEMultipart()
        msg['From'] = self.email_credentials['from']
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = 'Upcoming Holy Event Notification'
        body = f'There is an upcoming holy event: {event}'
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(self.email_credentials['smtp_server'], self.email_credentials['smtp_port'])
            server.starttls()
            server.login(self.email_credentials['username'], self.email_credentials['password'])
            server.sendmail(self.email_credentials['from'], self.recipients, msg.as_string())
        finally:
            server.quit()
