# Contributing to Starztech AI Bot

Thank you for your interest in contributing to Starztech AI Bot! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected behavior vs actual behavior
- Bot logs (if applicable)
- Environment details (Python version, OS, etc.)

### Suggesting Features

We welcome feature suggestions! Please create an issue with:
- Clear description of the feature
- Use case and benefits
- Any implementation ideas (optional)

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation if needed

4. **Test your changes**
   ```bash
   python test_config.py
   python bot.py  # Test locally
   ```

5. **Commit your changes**
   ```bash
   git commit -m "Add: your feature description"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Describe your changes
   - Reference any related issues
   - Add screenshots if applicable

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Lemonsupqt/Starztech.git
   cd Starztech
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your test credentials
   ```

4. **Run the bot**
   ```bash
   python bot.py
   ```

## Code Style Guidelines

- Use Python 3.11+ features
- Follow PEP 8 style guide
- Use type hints where appropriate
- Keep functions focused and small
- Add docstrings to functions
- Use meaningful variable names

## Testing

Before submitting a PR:

- [ ] Run `python test_config.py` successfully
- [ ] Test bot locally with test credentials
- [ ] Test all modified features
- [ ] Verify no new errors in logs
- [ ] Update documentation if needed

## Areas We Need Help

- 🎨 UI/UX improvements for bot messages
- 📝 Documentation improvements
- 🐛 Bug fixes
- ✨ New features
- 🌍 Internationalization/translations
- 🧪 Testing infrastructure
- 📊 Usage analytics
- 💾 Database integration for persistent storage

## Questions?

Feel free to:
- Open an issue for questions
- Contact via [@starztechbot](https://t.me/starztechbot)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for making Starztech AI Bot better! 🙏**
