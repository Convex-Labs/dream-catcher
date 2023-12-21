# Holy Event Notifier

## Purpose
The Holy Event Notifier is a project designed to monitor the Drik Panchang website for important holy events and send email notifications to a list of recipients whenever such events are upcoming.

## Design
The project consists of a single node, `EventMonitorNode`, which is responsible for periodically checking the Drik Panchang website for new event listings. When a new event is detected, the node sends out an email to all configured recipients with the details of the event.

The node uses the `requests` library to fetch the webpage with a specified timeout to prevent hanging requests and `BeautifulSoup` for parsing the HTML content to extract event details. Email notifications are sent using the `smtplib` and `email` libraries, with proper exception handling to ensure the server is always properly closed.

## Pipeline
The pipeline configuration is defined in `pipeline.yml` and includes the `EventMonitorNode` with its required parameters such as the URL to monitor, email credentials for sending notifications, and the list of recipients. The pipeline is designed to run with minimal resources, requiring only 0.5 CPUs as specified in the `default_node_settings`.

To ensure the pipeline runs effectively, it is important to configure the correct URL for the Drik Panchang website and provide valid email credentials for the notification system. The recipients' email addresses should also be correctly listed to ensure they receive the notifications.

## Usage
To use the Holy Event Notifier, simply deploy the pipeline and ensure that the environment is configured with the necessary dependencies. The node will handle the rest, periodically checking for events and sending notifications as needed.

## Conclusion
The Holy Event Notifier is a simple yet powerful tool for staying informed about important holy events. Its straightforward design and easy configuration make it an ideal solution for individuals and communities looking to keep track of such events.
