import logging
import nest_asyncio
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

telegram_bot_token = "7310153247:AAEvqWA3Crll_KHOzM1l_EedK0DL2LkSCck"
nest_asyncio.apply()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

model_name = "openai-community/gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

metadata_generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Welcome to CyborgSam! The one and only Metadata Generator. Give me same incomplete text!')

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Send any text, and I will generate metadata.')

async def generate_metadata(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    try:
        generated_text = metadata_generator(user_input, max_length=100, num_return_sequences=1)[0]['generated_text']
        await update.message.reply_text(f'Generated Metadata:\n{generated_text}')
    except Exception as e:
        logger.error(f'Error generating metadata: {e}')
        await update.message.reply_text('Sorry, there was an error processing your request.')

telegram_bot_token = telegram_bot_token
application = Application.builder().token(telegram_bot_token).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_metadata))

application.run_polling()