# Sales Funnel Automation

This project automates the sales funnel process using AI. It fetches data from a CRM system, composes personalized emails based on the CRM data, and sends them out to potential customers.

## Nodes

### CRMDataFetcher
This node is responsible for fetching data from the CRM system. It produces the data to the 'crm_data' dataset for further processing.

### EmailComposer
The EmailComposer node consumes CRM data and composes personalized emails. The composed emails are produced to the 'composed_email' dataset.

### EmailSender
The EmailSender node consumes the composed emails and sends them out to the respective recipients.

## Pipeline
The pipeline is configured to run these nodes in sequence, ensuring that CRM data is fetched, emails are composed, and then sent out. The datasets 'crm_data' and 'composed_email' act as the communication channels between these nodes.