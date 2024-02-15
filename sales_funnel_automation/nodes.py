from aineko.core.node import AbstractNode


class CRMDataFetcher(AbstractNode):
    def _pre_loop_hook(self, params=None):
        # Initialize any state or connections here
        pass

    def _execute(self, params=None):
        # Fetch CRM data and produce it to the 'crm_data' dataset
        crm_data = self.fetch_crm_data()
        self.producers['crm_data'].produce(crm_data)

    def fetch_crm_data(self):
        # Implement CRM data fetching logic
        return {}


class EmailComposer(AbstractNode):
    def _execute(self, params=None):
        crm_record = self.consumers['crm_data'].next()
        email_content = self.compose_email(crm_record)
        self.producers['composed_email'].produce(email_content)

    def compose_email(self, crm_record):
        # Implement email composition logic
        return 'Email content based on CRM record'


class EmailSender(AbstractNode):
    def _execute(self, params=None):
        email_content = self.consumers['composed_email'].next()
        self.send_email(email_content)

    def send_email(self, email_content):
        # Implement email sending logic
        pass