# Starztech AI Bot 🤖

An advanced multi-model Telegram chatbot powered by MegaLLM API with support for direct messages, groups, and **inline mode**.

## ✨ Features

- 🤖 **Multi-Model AI Support** - Choose from GPT-4, Claude, Gemini, and more
- 💬 **Direct Messages** - Chat privately with the AI
- 👥 **Group Chats** - Add the bot to groups (responds when mentioned)
- ⚡ **Inline Mode** - Get AI responses in ANY chat without leaving (just type `@starztechbot your question`)
- 🧠 **Context Awareness** - Remembers conversation history
- 🚀 **Railway Deployment Ready** - Easy deployment to Railway.com

## 🎯 Inline Mode - The Star Feature

The inline mode allows you to use AI assistance **anywhere** in Telegram:

```
@starztechbot what is quantum computing?
@starztechbot explain like I'm 5: how does the internet work?
@starztechbot write a python function to sort a list
```

Just type `@starztechbot` followed by your question in any chat, and you'll get instant AI-powered responses!

## 🚀 Setup

### Prerequisites

- Python 3.9 or higher
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- MegaLLM API Key (from [megallm.io](https://megallm.io/))
- Railway.com account (for hosting)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Lemonsupqt/Starztech.git
   cd Starztech
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   
   Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your credentials:
   ```env
   BOT_TOKEN=your_bot_token_from_botfather
   MEGALLM_API_KEY=your_megallm_api_key
   MEGALLM_API_URL=https://api.megallm.io/v1/chat/completions
   DEFAULT_MODEL=gpt-4
   MAX_TOKENS=2000
   TEMPERATURE=0.7
   ```

4. **Enable Inline Mode in BotFather**
   
   This is crucial for inline functionality:
   - Open [@BotFather](https://t.me/botfather) in Telegram
   - Send `/mybots`
   - Select your bot (@starztechbot)
   - Choose "Bot Settings" → "Inline Mode"
   - Click "Turn on"
   - Optionally set an inline placeholder like "Ask me anything..."

5. **Run the bot**
   ```bash
   python bot.py
   ```

### Railway Deployment

1. **Connect your GitHub repository to Railway**
   - Go to [Railway.com](https://railway.com)
   - Create a new project
   - Connect your GitHub repository

2. **Add environment variables**
   
   In Railway dashboard, add these variables:
   - `BOT_TOKEN` - Your Telegram bot token
   - `MEGALLM_API_KEY` - Your MegaLLM API key
   - `MEGALLM_API_URL` - API endpoint (optional, defaults to megallm.io)
   - `DEFAULT_MODEL` - Default AI model (optional, defaults to gpt-4)

3. **Deploy**
   
   Railway will automatically detect the configuration and deploy using:
   - `railway.json` for deployment settings
   - `Procfile` for the start command
   - `requirements.txt` for dependencies

## 📖 Usage

### Commands

- `/start` - Welcome message and introduction
- `/help` - Detailed help and usage instructions
- `/model <model_name>` - Switch AI model (e.g., `/model claude-3-opus`)
- `/models` - List all available models
- `/clear` - Clear conversation history

### In Direct Messages (DM)

Simply send any message to the bot:

```
User: What is artificial intelligence?
Bot: Artificial intelligence (AI) refers to...
```

### In Group Chats

Mention the bot or reply to its messages:

```
User: @starztechbot explain quantum computing
Bot: Quantum computing is a type of computation...
```

### Inline Mode (Use Anywhere!)

Type `@starztechbot` in any chat:

```
@starztechbot how do I center a div in CSS?
```

Select the AI response from the dropdown and it will be sent to the chat!

## 🤖 Available Models

- **OpenAI**
  - `gpt-4` - Most capable (default)
  - `gpt-3.5-turbo` - Fast and efficient

- **Anthropic**
  - `claude-3-opus` - Most powerful
  - `claude-3-sonnet` - Balanced
  - `claude-3-haiku` - Fast

- **Google**
  - `gemini-pro` - Google's flagship model

Switch models anytime with `/model <model_name>`

## 🛠️ Technical Details

### Architecture

- **Framework**: python-telegram-bot 20.7
- **API Client**: aiohttp for async HTTP requests
- **Environment**: python-dotenv for configuration
- **Deployment**: Railway.com with Procfile

### Key Features Implementation

- **Conversation History**: Stored in-memory per user (last 10 messages)
- **Inline Mode**: Full support with multiple response formats
- **Group Support**: Responds only when mentioned or replied to
- **Error Handling**: Comprehensive logging and graceful error responses
- **Async Operations**: All API calls and handlers are async for performance

## 📝 Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `BOT_TOKEN` | Telegram bot token from BotFather | ✅ Yes | - |
| `MEGALLM_API_KEY` | MegaLLM API key | ✅ Yes | - |
| `MEGALLM_API_URL` | MegaLLM API endpoint | ❌ No | `https://api.megallm.io/v1/chat/completions` |
| `DEFAULT_MODEL` | Default AI model | ❌ No | `gpt-4` |
| `MAX_TOKENS` | Max tokens per response | ❌ No | `2000` |
| `TEMPERATURE` | AI temperature (0-1) | ❌ No | `0.7` |

## 🔒 Security

- API keys are stored as environment variables
- No sensitive data is logged
- Conversation history is stored in-memory (not persisted)
- Use environment variables for all credentials

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Credits

- Powered by [MegaLLM](https://megallm.io/)
- Built with [python-telegram-bot](https://python-telegram-bot.org/)
- Deployed on [Railway.com](https://railway.com/)

## 📧 Support

For issues and questions:
- Open an issue on GitHub
- Contact: [@starztechbot](https://t.me/starztechbot)

---

**Made with ❤️ by Starztech**
