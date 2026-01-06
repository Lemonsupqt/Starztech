#!/usr/bin/env python3
"""
Starztech AI Bot - Advanced Multi-Model Telegram Chatbot
Supports DM, Groups, and Inline Mode with MegaLLM API integration
"""

import os
import logging
from typing import Dict, List
from uuid import uuid4
from dotenv import load_dotenv

from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    InlineQueryHandler,
    ContextTypes,
    filters,
)
import aiohttp

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
MEGALLM_API_KEY = os.getenv('MEGALLM_API_KEY')
MEGALLM_API_URL = os.getenv('MEGALLM_API_URL', 'https://api.megallm.io/v1/chat/completions')
DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'gpt-4')
MAX_TOKENS = int(os.getenv('MAX_TOKENS', '2000'))
TEMPERATURE = float(os.getenv('TEMPERATURE', '0.7'))

# Store conversation history per user
conversation_history: Dict[int, List[Dict]] = {}
user_models: Dict[int, str] = {}


async def call_megallm_api(messages: List[Dict], model: str = None) -> str:
    """Call MegaLLM API to get AI response"""
    if not model:
        model = DEFAULT_MODEL
    
    headers = {
        'Authorization': f'Bearer {MEGALLM_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'model': model,
        'messages': messages,
        'max_tokens': MAX_TOKENS,
        'temperature': TEMPERATURE
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(MEGALLM_API_URL, json=data, headers=headers) as response:
                if response.status == 200:
                    result = await response.json()
                    return result['choices'][0]['message']['content']
                else:
                    error_text = await response.text()
                    logger.error(f"API Error: {response.status} - {error_text}")
                    return f"Sorry, I encountered an error: {response.status}"
    except Exception as e:
        logger.error(f"Exception calling API: {e}")
        return f"Sorry, I encountered an error: {str(e)}"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    welcome_message = f"""
🌟 Welcome to Starztech AI Bot, {user.first_name}! 🌟

I'm an advanced multi-model chatbot powered by MegaLLM.

📱 **How to use me:**
• **In DMs**: Just send me a message and I'll respond
• **In Groups**: Mention me or reply to my messages
• **Inline Mode**: Type `@starztechbot your question` in any chat!

⚙️ **Available Commands:**
/start - Show this welcome message
/help - Get help and usage information
/model - Change AI model
/clear - Clear conversation history
/models - List available models

🚀 **Inline Mode** is perfect for quick questions without leaving your current chat!

Try it now: Type `@starztechbot what is AI?` in any chat!
"""
    await update.message.reply_text(welcome_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = """
🆘 **Starztech AI Bot Help**

**Basic Usage:**
• Send me any message and I'll respond using AI
• I remember context within our conversation
• Use /clear to start fresh

**Commands:**
• /start - Welcome message
• /help - This help message
• /model <model_name> - Switch AI model
• /models - List available models
• /clear - Clear conversation history

**Inline Mode:**
Type `@starztechbot` followed by your question in ANY chat:
• `@starztechbot what is quantum computing?`
• `@starztechbot explain like I'm 5: blockchain`
• `@starztechbot write a haiku about code`

The inline mode will show you the AI response instantly!

**Available Models:**
• gpt-4 (default) - Most capable
• gpt-3.5-turbo - Faster responses
• claude-3-opus - Advanced reasoning
• claude-3-sonnet - Balanced performance
• gemini-pro - Google's model

**Tips:**
• Be specific with your questions
• For coding help, mention the programming language
• Use inline mode for quick answers
"""
    await update.message.reply_text(help_text)


async def models_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """List available AI models."""
    models_text = """
🤖 **Available AI Models:**

**OpenAI Models:**
• `gpt-4` - Most capable model (default)
• `gpt-3.5-turbo` - Fast and efficient

**Anthropic Models:**
• `claude-3-opus` - Most powerful Claude
• `claude-3-sonnet` - Balanced performance
• `claude-3-haiku` - Fast responses

**Google Models:**
• `gemini-pro` - Google's flagship model

**Usage:**
Use `/model <model_name>` to switch models.
Example: `/model claude-3-opus`

**Current Model:**
"""
    user_id = update.effective_user.id
    current_model = user_models.get(user_id, DEFAULT_MODEL)
    models_text += f"`{current_model}`"
    
    await update.message.reply_text(models_text)


async def model_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Change the AI model for the user."""
    user_id = update.effective_user.id
    
    if not context.args:
        current_model = user_models.get(user_id, DEFAULT_MODEL)
        await update.message.reply_text(
            f"Current model: `{current_model}`\n\n"
            f"To change model, use: `/model <model_name>`\n"
            f"Use /models to see available models."
        )
        return
    
    new_model = context.args[0]
    user_models[user_id] = new_model
    await update.message.reply_text(f"✅ Model changed to: `{new_model}`")


async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Clear conversation history for the user."""
    user_id = update.effective_user.id
    if user_id in conversation_history:
        del conversation_history[user_id]
    await update.message.reply_text("🗑️ Conversation history cleared!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming messages (DM and Groups)."""
    user_id = update.effective_user.id
    message_text = update.message.text
    
    # In groups, only respond if mentioned or replied to
    if update.message.chat.type in ['group', 'supergroup']:
        bot_username = context.bot.username
        # Check if bot is mentioned
        if f"@{bot_username}" not in message_text:
            # Check if message is a reply to the bot
            if not (update.message.reply_to_message and 
                   update.message.reply_to_message.from_user.id == context.bot.id):
                return
        # Remove bot mention from message
        message_text = message_text.replace(f"@{bot_username}", "").strip()
    
    # Initialize conversation history if needed
    if user_id not in conversation_history:
        conversation_history[user_id] = []
    
    # Add user message to history
    conversation_history[user_id].append({
        'role': 'user',
        'content': message_text
    })
    
    # Keep only last 10 messages for context (5 exchanges)
    if len(conversation_history[user_id]) > 10:
        conversation_history[user_id] = conversation_history[user_id][-10:]
    
    # Show typing indicator
    await update.message.chat.send_action(action="typing")
    
    # Get model for user
    model = user_models.get(user_id, DEFAULT_MODEL)
    
    # Get AI response
    response = await call_megallm_api(conversation_history[user_id], model)
    
    # Add assistant response to history
    conversation_history[user_id].append({
        'role': 'assistant',
        'content': response
    })
    
    # Send response
    await update.message.reply_text(response)


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle inline queries - KEY FEATURE for inline mode."""
    query = update.inline_query.query
    
    if not query or len(query.strip()) < 3:
        # Show help message if query is too short
        results = [
            InlineQueryResultArticle(
                id=str(uuid4()),
                title="Ask me anything!",
                description="Type your question after @starztechbot",
                input_message_content=InputTextMessageContent(
                    message_text="💡 Tip: Type your question after @starztechbot to get AI-powered answers instantly!"
                )
            )
        ]
        await update.inline_query.answer(results, cache_time=300)
        return
    
    user_id = update.inline_query.from_user.id
    
    # Get model for user
    model = user_models.get(user_id, DEFAULT_MODEL)
    
    # Create a simple message for the API (no history in inline mode for simplicity)
    messages = [{'role': 'user', 'content': query}]
    
    # Get AI response
    response = await call_megallm_api(messages, model)
    
    # Create inline results
    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title=f"AI Response ({model})",
            description=response[:100] + "..." if len(response) > 100 else response,
            input_message_content=InputTextMessageContent(
                message_text=f"**Question:** {query}\n\n**Answer:**\n{response}\n\n_Powered by Starztech AI_"
            )
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Short Answer",
            description="Get a concise response",
            input_message_content=InputTextMessageContent(
                message_text=f"Q: {query}\n\nA: {response}\n\n_via @starztechbot_"
            )
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Question Only",
            description="Send just your question",
            input_message_content=InputTextMessageContent(
                message_text=f"❓ {query}"
            )
        )
    ]
    
    # Answer the inline query
    await update.inline_query.answer(results, cache_time=300)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors caused by updates."""
    logger.error(f"Update {update} caused error {context.error}")


def main() -> None:
    """Start the bot."""
    # Validate configuration
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN not found in environment variables!")
        return
    
    if not MEGALLM_API_KEY:
        logger.error("MEGALLM_API_KEY not found in environment variables!")
        return
    
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("model", model_command))
    application.add_handler(CommandHandler("models", models_command))
    application.add_handler(CommandHandler("clear", clear_command))
    
    # Inline query handler - CRITICAL for inline mode
    application.add_handler(InlineQueryHandler(inline_query))
    
    # Message handler for DM and Groups
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Error handler
    application.add_error_handler(error_handler)
    
    # Start the Bot
    logger.info("Starting Starztech AI Bot...")
    logger.info(f"Default model: {DEFAULT_MODEL}")
    logger.info("Inline mode enabled!")
    
    # Run the bot using polling
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
