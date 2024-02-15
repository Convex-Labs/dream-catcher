# SlackBot Project

This project contains a SlackBot that interacts with users on Slack. It listens for messages on a specified channel and can respond to users based on the logic implemented within the bot.

## Design

The `SlackBotNode` is the core of the project, which inherits from `AbstractNode`. It uses the `_pre_loop_hook` to initialize the Slack client with the necessary credentials and channel information. The `_execute` method contains the main logic for the bot, which listens for messages and responds accordingly. The `_post_loop_hook` is used for cleaning up resources when the bot is shutting down.

## Pipeline

The pipeline configuration in `pipeline.yml` defines the `slack_bot` node and its parameters, such as the Slack token and channel. It also defines a `slack_messages` dataset, which is a Kafka stream that the bot uses to receive and send messages.
