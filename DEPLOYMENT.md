# 🚀 Deployment Checklist for @starztechbot

This checklist will guide you through deploying your bot to Railway.com and making it operational.

## ✅ Pre-Deployment Checklist

### 1. Bot Configuration in BotFather

- [ ] Open [@BotFather](https://t.me/botfather) in Telegram
- [ ] Send `/mybots`
- [ ] Select @starztechbot
- [ ] Get/verify bot token from "API Token"
- [ ] **CRITICAL**: Enable Inline Mode
  - [ ] Go to "Bot Settings" → "Inline Mode" → "Turn on"
  - [ ] Set inline placeholder (optional): "Ask me anything..."
  - [ ] Enable inline feedback: ON
- [ ] Set bot description (optional but recommended)
- [ ] Set bot about text (optional)
- [ ] Set bot profile picture (optional)

### 2. MegaLLM API Setup

- [ ] Log in to [megallm.io](https://megallm.io/)
- [ ] Navigate to API Keys section
- [ ] Copy your API key
- [ ] Verify your subscription is active (you mentioned max subscription ✅)
- [ ] Note the API endpoint (usually `https://api.megallm.io/v1/chat/completions`)

### 3. GitHub Repository

- [ ] Ensure all files are pushed to GitHub
  - [ ] bot.py
  - [ ] requirements.txt
  - [ ] Procfile
  - [ ] railway.json
  - [ ] runtime.txt
  - [ ] .gitignore
  - [ ] README.md
  - [ ] SETUP.md
  - [ ] INLINE_GUIDE.md

## 🚂 Railway Deployment Steps

### Option A: Deploy via Railway Web Dashboard (Recommended)

#### Step 1: Create New Project

- [ ] Go to [railway.app](https://railway.app/)
- [ ] Click "New Project"
- [ ] Select "Deploy from GitHub repo"
- [ ] Authenticate with GitHub if needed
- [ ] Select repository: `Lemonsupqt/Starztech`
- [ ] Select branch: `main` (or your working branch)

#### Step 2: Configure Environment Variables

Click on your project, then go to "Variables" tab:

**Required Variables:**
- [ ] Add `BOT_TOKEN` = `[your bot token from BotFather]`
- [ ] Add `MEGALLM_API_KEY` = `[your megallm api key]`

**Optional Variables** (use these if you want to customize):
- [ ] Add `MEGALLM_API_URL` = `https://api.megallm.io/v1/chat/completions`
- [ ] Add `DEFAULT_MODEL` = `gpt-4`
- [ ] Add `MAX_TOKENS` = `2000`
- [ ] Add `TEMPERATURE` = `0.7`

#### Step 3: Deploy

- [ ] Click "Deploy"
- [ ] Wait for build to complete (watch logs)
- [ ] Check for "Build successful" message
- [ ] Verify deployment status is "Active"

#### Step 4: Monitor Logs

- [ ] Click on "Deployments" tab
- [ ] Click on the latest deployment
- [ ] View logs to ensure bot started successfully
- [ ] Look for messages like:
  ```
  Starting Starztech AI Bot...
  Default model: gpt-4
  Inline mode enabled!
  ```

### Option B: Deploy via Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Link to your project (in repo directory)
cd /path/to/Starztech
railway link

# Set environment variables
railway variables set BOT_TOKEN="your_bot_token_here"
railway variables set MEGALLM_API_KEY="your_api_key_here"

# Deploy
railway up

# Check logs
railway logs
```

## 🧪 Testing Checklist

### Test 1: Basic Functionality

- [ ] Open Telegram
- [ ] Search for `@starztechbot`
- [ ] Send `/start` command
- [ ] Verify welcome message appears
- [ ] Send a simple question: "What is AI?"
- [ ] Verify you receive an AI response

### Test 2: Direct Message Features

- [ ] Send `/help` - verify help message
- [ ] Send `/models` - verify model list
- [ ] Send `/model gpt-3.5-turbo` - verify model change confirmation
- [ ] Ask a question - verify response uses new model
- [ ] Send `/clear` - verify history cleared message

### Test 3: Inline Mode (CRITICAL!)

- [ ] Open any chat in Telegram (even "Saved Messages")
- [ ] Type: `@starztechbot what is 2+2?`
- [ ] Wait for dropdown to appear with AI response
- [ ] Verify you see multiple result options
- [ ] Select a result
- [ ] Verify message is sent to the chat
- [ ] Try another query: `@starztechbot tell me a joke`
- [ ] Verify it works consistently

### Test 4: Group Chat Features

- [ ] Create a test group or use existing one
- [ ] Add @starztechbot to the group
- [ ] Send message: `@starztechbot hello`
- [ ] Verify bot responds
- [ ] Send message without mention
- [ ] Verify bot does NOT respond
- [ ] Send message replying to bot's previous message
- [ ] Verify bot responds

### Test 5: Model Switching

- [ ] In DM, send `/model claude-3-opus`
- [ ] Ask a question
- [ ] Verify response (may have different style)
- [ ] Try `/model gemini-pro`
- [ ] Ask another question
- [ ] Switch back: `/model gpt-4`

### Test 6: Conversation Context

- [ ] Start a conversation: "My name is John"
- [ ] Follow up: "What is my name?"
- [ ] Verify bot remembers (should say "John")
- [ ] Send `/clear`
- [ ] Ask again: "What is my name?"
- [ ] Verify bot doesn't remember (history cleared)

## 🔍 Troubleshooting

### Bot doesn't respond to commands

**Possible Issues:**
- [ ] Check Railway logs for errors
- [ ] Verify BOT_TOKEN is correct
- [ ] Restart deployment in Railway
- [ ] Check if bot is blocked in Telegram

**Fix:**
```bash
# In Railway dashboard
1. Go to Deployments
2. Click on latest deployment
3. Click "Restart"
4. Monitor logs
```

### Inline mode doesn't work

**Possible Issues:**
- [ ] Inline mode not enabled in BotFather ❗ MOST COMMON
- [ ] Wrong bot username
- [ ] Bot not running on Railway
- [ ] Query too short (< 3 characters)

**Fix:**
1. Open @BotFather
2. /mybots → @starztechbot
3. Bot Settings → Inline Mode → Turn on
4. Try again: `@starztechbot test query`

### API errors in responses

**Possible Issues:**
- [ ] MEGALLM_API_KEY is incorrect
- [ ] API subscription expired
- [ ] API rate limit reached
- [ ] Network issues

**Fix:**
1. Verify API key in Railway variables
2. Check megallm.io subscription status
3. Check Railway logs for specific error
4. Contact megallm.io support if needed

### Bot stops responding after a while

**Possible Issues:**
- [ ] Railway deployment crashed
- [ ] Out of memory
- [ ] API timeout

**Fix:**
```bash
# Check Railway logs
railway logs

# Restart deployment
# In Railway dashboard: Deployments → Restart

# If persistent, check Railway plan limits
```

## 📊 Monitoring

### Daily Checks

- [ ] Check Railway dashboard - verify deployment is "Active"
- [ ] Test bot with simple command: `/start`
- [ ] Test inline mode: `@starztechbot test`
- [ ] Review Railway logs for errors

### Weekly Checks

- [ ] Review Railway usage metrics
- [ ] Check megallm.io usage/credits
- [ ] Test all features (DM, group, inline)
- [ ] Update dependencies if needed

## 🎉 Post-Deployment

### Share Your Bot

Once everything works:

- [ ] Share bot link: `https://t.me/starztechbot`
- [ ] Promote inline mode feature
- [ ] Create tutorial/demo video (optional)
- [ ] Add bot to your groups

### Promote Inline Mode

Example messages to share:

```
🌟 Check out @starztechbot!

Use it ANYWHERE in Telegram:
@starztechbot what is quantum computing?
@starztechbot write a haiku about code
@starztechbot explain AI in simple terms

No need to add the bot - just type @starztechbot and your question!
```

## 📝 Notes

- Railway Pro subscription ✅ (you have this)
- MegaLLM max subscription ✅ (you have this)
- Bot token for @starztechbot ✅ (you have this)

**You have everything you need! Just follow this checklist step by step.**

## 🆘 Need Help?

If you encounter issues:

1. Check Railway logs first
2. Review this checklist
3. Check SETUP.md for detailed setup
4. Check INLINE_GUIDE.md for inline mode details
5. Open a GitHub issue with:
   - Description of the problem
   - Railway logs (if applicable)
   - Steps to reproduce

---

**Good luck with your deployment! 🚀**

Once deployed, try: `@starztechbot tell me something amazing!`
