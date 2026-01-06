# Starztech AI Bot - Setup Guide

## Quick Start for @starztechbot

### 1. Configure Bot Token

You mentioned the bot name is `@starztechbot`. Here's how to get/verify the token:

1. Open [@BotFather](https://t.me/botfather) in Telegram
2. Send `/mybots`
3. Select @starztechbot
4. Click "API Token" to view/regenerate your token
5. Copy the token (format: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 2. Enable Inline Mode (CRITICAL!)

**This step is essential for inline functionality:**

1. Open [@BotFather](https://t.me/botfather)
2. Send `/mybots`
3. Select @starztechbot
4. Choose "Bot Settings"
5. Click "Inline Mode"
6. Click "Turn on"
7. Optionally:
   - Set inline placeholder: "Ask me anything..."
   - Enable inline feedback: ON

### 3. Get MegaLLM API Key

Since you have a max subscription:

1. Go to [megallm.io](https://megallm.io/)
2. Log in to your account
3. Navigate to API Keys section
4. Copy your API key

### 4. Deploy to Railway

#### Option A: Deploy via GitHub (Recommended)

1. Push this code to your GitHub repository
2. Go to [Railway.com](https://railway.com)
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Add environment variables:
   ```
   BOT_TOKEN=your_actual_bot_token
   MEGALLM_API_KEY=your_actual_megallm_key
   ```
7. Click "Deploy"

#### Option B: Deploy via CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Initialize project
railway init

# Add environment variables
railway variables set BOT_TOKEN=your_actual_bot_token
railway variables set MEGALLM_API_KEY=your_actual_megallm_key

# Deploy
railway up
```

### 5. Verify Deployment

1. Check Railway logs to ensure bot started successfully
2. Send `/start` to @starztechbot in Telegram
3. Test inline mode: Type `@starztechbot test` in any chat

## Testing Checklist

### DM Testing
- [ ] Send `/start` - Should receive welcome message
- [ ] Send a question - Should receive AI response
- [ ] Send `/models` - Should list available models
- [ ] Send `/model gpt-3.5-turbo` - Should confirm model change
- [ ] Send another question - Should use new model
- [ ] Send `/clear` - Should clear history

### Group Testing
- [ ] Add @starztechbot to a test group
- [ ] Send `@starztechbot hello` - Should respond
- [ ] Reply to bot's message - Should respond
- [ ] Send message without mention - Should NOT respond

### Inline Testing (MOST IMPORTANT!)
- [ ] In any chat, type: `@starztechbot what is AI?`
- [ ] Should see dropdown with AI response
- [ ] Select response - Should send to chat
- [ ] Try different queries
- [ ] Verify responses are accurate

## Troubleshooting

### Bot doesn't respond
- Check Railway logs for errors
- Verify BOT_TOKEN is correct
- Ensure bot is not blocked

### Inline mode doesn't work
- Verify inline mode is enabled in BotFather
- Check if you're typing the correct username: `@starztechbot`
- Ensure bot is running (check Railway logs)

### API errors
- Verify MEGALLM_API_KEY is correct
- Check MegaLLM subscription status
- Review Railway logs for specific error messages

### Railway deployment fails
- Check Railway logs for build errors
- Verify all dependencies in requirements.txt
- Ensure Python version is compatible (3.9+)

## Advanced Configuration

### Custom Models

Edit environment variables in Railway:

```
DEFAULT_MODEL=claude-3-opus
MAX_TOKENS=4000
TEMPERATURE=0.5
```

### API Endpoint

If using a different MegaLLM endpoint:

```
MEGALLM_API_URL=https://custom-api.megallm.io/v1/chat/completions
```

## Support

If you encounter issues:

1. Check Railway logs
2. Review Telegram bot settings in BotFather
3. Verify API key validity on megallm.io
4. Check GitHub issues for similar problems

## Next Steps

After successful deployment:

1. Customize welcome message in `bot.py` (optional)
2. Add more models if needed
3. Implement usage tracking (optional)
4. Add admin commands (optional)
5. Share your bot with friends!

---

**Your bot @starztechbot is ready to use! 🚀**
