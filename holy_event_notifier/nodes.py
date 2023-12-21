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
        self.request_timeout = params.get('request_timeout', 10)  # Default timeout of 10 seconds

    def _execute(self, params: Optional[dict] = None):
        try:
            response = requests.get(self.url, timeout=self.request_timeout)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                events = self.extract_events(soup)
                if events:
                    self.send_email(events)
        except requests.RequestException as e:
            self.log(f'Error fetching the webpage: {e}', level='error')

    def extract_events(self, soup):
        # This method should be implemented to extract events from the Drik Panchang website
        # For the sake of this example, let's assume we have a simple way to identify events
        events_list = soup.find_all(class_='important-holy-event')
        return [event.get_text() for event in events_list]

    def send_email(self, events):
        msg = MIMEMultipart()
        msg['From'] = self.email_credentials['from']
        msg['To'] = self.email_credentials['to']
        msg['Subject'] = 'Upcoming Holy Events Notification'
        body = '\n'.join(events)
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(self.email_credentials['smtp_server'], self.email_credentials['smtp_port'])
            server.starttls()
            server.login(msg['From'], self.email_credentials['password'])
            server.sendmail(msg['From'], msg['To'], msg.as_string())
        finally:
            server.quit()
