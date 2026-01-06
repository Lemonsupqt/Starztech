#!/usr/bin/env python3
"""
Test script to verify bot configuration and dependencies
"""

import sys
import os

# Placeholder constants
DEFAULT_BOT_TOKEN = 'your_bot_token_here'
DEFAULT_API_KEY = 'your_megallm_api_key_here'


def test_imports():
    """Test if all required packages can be imported"""
    print("Testing imports...")
    
    try:
        import telegram
        print("✅ python-telegram-bot imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import telegram: {e}")
        return False
    
    try:
        import aiohttp
        print("✅ aiohttp imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import aiohttp: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import dotenv: {e}")
        return False
    
    try:
        import requests
        print("✅ requests imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import requests: {e}")
        return False
    
    return True


def test_env_file():
    """Test if .env file exists and is readable"""
    print("\nTesting environment configuration...")
    
    if os.path.exists('.env'):
        print("✅ .env file found")
        from dotenv import load_dotenv
        load_dotenv()
        
        # Check required variables
        bot_token = os.getenv('BOT_TOKEN')
        api_key = os.getenv('MEGALLM_API_KEY')
        
        if bot_token and bot_token != DEFAULT_BOT_TOKEN:
            print("✅ BOT_TOKEN is configured")
        else:
            print("⚠️  BOT_TOKEN is not configured (using default/placeholder)")
        
        if api_key and api_key != DEFAULT_API_KEY:
            print("✅ MEGALLM_API_KEY is configured")
        else:
            print("⚠️  MEGALLM_API_KEY is not configured (using default/placeholder)")
        
    else:
        print("⚠️  .env file not found (will use environment variables or defaults)")
    
    return True


def test_bot_file():
    """Test if bot.py exists and is valid Python"""
    print("\nTesting bot.py...")
    
    if not os.path.exists('bot.py'):
        print("❌ bot.py not found")
        return False
    
    print("✅ bot.py found")
    
    # Try to compile it
    try:
        with open('bot.py', 'r') as f:
            code = f.read()
            compile(code, 'bot.py', 'exec')
        print("✅ bot.py syntax is valid")
    except SyntaxError as e:
        print(f"❌ bot.py has syntax errors: {e}")
        return False
    
    return True


def main():
    """Run all tests"""
    print("=" * 50)
    print("Starztech AI Bot - Configuration Test")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("Environment Test", test_env_file),
        ("Bot File Test", test_bot_file),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 50)
    print("Test Summary")
    print("=" * 50)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(result for _, result in results)
    
    if all_passed:
        print("\n🎉 All tests passed! Bot is ready to run.")
        print("\nNext steps:")
        print("1. Configure .env with your BOT_TOKEN and MEGALLM_API_KEY")
        print("2. Enable inline mode in @BotFather")
        print("3. Run: python bot.py")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
