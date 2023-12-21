# Holy Event Notifier

The Holy Event Notifier is a project designed to monitor the Drik Panchang website for important holy events and send email notifications to subscribed users when such events are upcoming.

## Design

The project consists of a single node, `EventMonitorNode`, which is responsible for fetching the webpage, extracting event information, and sending out the email notifications.

### EventMonitorNode

This node performs the following actions:

1. Fetches the Drik Panchang webpage using a GET request with a specified timeout to prevent hanging.
2. Parses the HTML content to extract details of important holy events.
3. Sends an email with the list of upcoming events to the specified recipient.

The node is configured to run with minimal CPU resources and does not interact with any input or output datasets, as its function is self-contained.

## Pipeline Configuration

The pipeline is defined in `pipeline.yml` with the following settings:

- Node class: `EventMonitorNode` from the `holy_event_notifier.nodes` module.
- Node parameters: URL of the Drik Panchang website, request timeout, and email credentials for sending notifications.

## Usage

To use this project, ensure that the email credentials are set correctly in the `pipeline.yml` file. The pipeline can then be executed using the Aineko framework, which will schedule and run the `EventMonitorNode` as defined.

## Future Enhancements

Future enhancements may include more sophisticated event extraction logic, support for multiple recipients, and configurable notification intervals.
