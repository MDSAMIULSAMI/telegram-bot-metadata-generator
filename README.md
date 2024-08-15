# CyborgSam: Telegram Bot for Metadata Generation

CyborgSam is a Telegram bot that generates metadata based on user input using a text-generation model. The bot leverages the GPT-2 model provided by the Hugging Face `transformers` library to create metadata from incomplete text sent by users.

## Features

- **/start**: Sends a welcome message explaining the bot's functionality.
- **/help**: Provides help on how to use the bot.
- **Metadata Generation**: The bot generates metadata from any text sent by the user.

## Installation

To run CyborgSam, you need to have Python installed on your system. Then, install the required Python libraries:

```bash
pip install python-telegram-bot transformers nest_asyncio
