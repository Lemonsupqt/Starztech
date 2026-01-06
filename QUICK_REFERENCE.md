# 📋 Quick Reference Card

## 🚀 Essential Commands

### Bot Commands (in DM with @starztechbot)
```
/start   - Welcome message and introduction
/help    - Detailed help and usage guide
/models  - List all available AI models
/model <name> - Switch to a different model (e.g., /model gpt-4)
/clear   - Clear conversation history
```

## ⚡ Inline Mode Usage

**Format:** `@starztechbot <your question>`

**Examples:**
```
@starztechbot what is AI?
@starztechbot how to center a div in CSS?
@starztechbot write a Python function to reverse a string
@starztechbot explain quantum physics in simple terms
@starztechbot translate "hello" to French
```

**Works in:** Any chat, group, or channel - no need to add the bot!

## 🤖 Available Models

| Model | Provider | Best For |
|-------|----------|----------|
| `gpt-4` | OpenAI | Most capable, complex tasks (default) |
| `gpt-3.5-turbo` | OpenAI | Fast responses, simple tasks |
| `claude-3-opus` | Anthropic | Advanced reasoning, long context |
| `claude-3-sonnet` | Anthropic | Balanced performance |
| `claude-3-haiku` | Anthropic | Very fast responses |
| `gemini-pro` | Google | Multimodal capabilities |
| `deepseek-chat` ⭐ | DeepSeek | General purpose, **unlimited usage** |
| `deepseek-coder` ⭐ | DeepSeek | Coding tasks, **unlimited usage** |
| `qwen-max` ⭐ | Qwen | Most capable, **unlimited usage** |
| `qwen-turbo` ⭐ | Qwen | Fast responses, **unlimited usage** |

## 🔧 Environment Variables

**Required:**
```env
BOT_TOKEN=your_bot_token_from_botfather
MEGALLM_API_KEY=your_megallm_api_key
```

**Optional:**
```env
MEGALLM_API_URL=https://api.megallm.io/v1/chat/completions
DEFAULT_MODEL=gpt-4
MAX_TOKENS=2000
TEMPERATURE=0.7
```

## 📁 Key Files

| File | Purpose |
|------|---------|
| `bot.py` | Main bot application |
| `requirements.txt` | Python dependencies |
| `Procfile` | Railway startup command |
| `railway.json` | Railway configuration |
| `runtime.txt` | Python version |
| `.env.example` | Environment template |
| `README.md` | Main documentation |
| `SETUP.md` | Detailed setup guide |
| `INLINE_GUIDE.md` | Inline mode tutorial |
| `DEPLOYMENT.md` | Deployment checklist |

## 🎯 Quick Start

### Local Testing
```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials
python bot.py
```

### Railway Deployment
```bash
railway login
railway link
railway variables set BOT_TOKEN="your_token"
railway variables set MEGALLM_API_KEY="your_key"
railway up
```

## ✅ Verification Steps

1. **Bot Active**: Send `/start` to @starztechbot
2. **DM Working**: Ask any question in DM
3. **Inline Working**: Type `@starztechbot test` in any chat
4. **Group Working**: Mention bot in a group
5. **Model Switching**: Try `/model gpt-3.5-turbo`

## 🔍 Common Issues & Fixes

### Inline Mode Not Working
**Fix:** Enable in @BotFather → Bot Settings → Inline Mode → Turn on

### Bot Not Responding
**Fix:** Check Railway logs, verify bot token, restart deployment

### API Errors
**Fix:** Verify MEGALLM_API_KEY, check subscription status

### Railway Build Failed
**Fix:** Check logs, verify requirements.txt, ensure Python 3.11

## 📱 Bot Capabilities

- ✅ Direct messages (1-on-1 chat)
- ✅ Group chats (responds when mentioned)
- ✅ Inline mode (use anywhere!)
- ✅ Multiple AI models
- ✅ Conversation context
- ✅ Model switching
- ✅ History management

## 🌟 Best Features

1. **Inline Mode** - Use AI anywhere without adding bot
2. **Multi-Model** - Switch between GPT, Claude, Gemini
3. **Context Aware** - Remembers conversation history
4. **Group Friendly** - Only responds when needed
5. **Always Available** - Hosted 24/7 on Railway

## 📞 Support Resources

- 📖 Full docs: `README.md`
- 🛠️ Setup guide: `SETUP.md`
- ⚡ Inline tutorial: `INLINE_GUIDE.md`
- 🚀 Deployment: `DEPLOYMENT.md`
- 🐛 Issues: GitHub Issues
- 💬 Bot: [@starztechbot](https://t.me/starztechbot)

## 🎨 Customization Tips

### Change Default Model
```env
DEFAULT_MODEL=claude-3-opus
```

### Adjust Response Length
```env
MAX_TOKENS=4000
```

### Modify Creativity
```env
TEMPERATURE=0.9  # More creative
TEMPERATURE=0.3  # More focused
```

## 🔐 Security Notes

- Never commit `.env` file (in `.gitignore`)
- Store secrets in Railway environment variables
- API keys are in environment only, not in code
- Conversation history is in-memory (not persisted)

## 💡 Pro Tips

1. **Inline Mode**: Best for quick questions in any chat
2. **DM Mode**: Best for longer conversations with context
3. **Model Selection**: Try different models for different tasks
4. **Clear History**: Use `/clear` to start fresh conversations
5. **Group Usage**: Mention bot only when needed to avoid spam

---

**🚀 Ready to use? Try it now:**
```
@starztechbot tell me something amazing!
```
