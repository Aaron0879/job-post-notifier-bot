# Job Post Notifier Bot

A Python-based automation bot that scrapes job portals for role-specific keywords and sends real-time notifications via Discord Webhooks.

## Technology Stack

- **Python 3.13+**
- **BeautifulSoup4**: HTML parsing and web scraping
- **Requests**: HTTP requests to fetch web pages
- **Schedule**: Task scheduling for periodic job checks
- **Discord Webhooks**: Real-time notifications

## Installation

### Prerequisites
- Python 3.7+ installed
- Git
- Discord server (free)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/job-post-notifier-bot.git
   cd job-post-notifier-bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your Discord Webhook URL**:
   - Open Discord and navigate to your server
   - Create a channel (e.g., `#job-alerts`)
   - Right-click the channel → Settings → Integrations → Webhooks
   - Click "New Webhook", copy the Webhook URL

4. **Configure the bot**:
   - Open `bot.py`
   - Replace `YOUR_DISCORD_WEBHOOK_URL_HERE` with your actual Discord Webhook URL
   - Update `TARGET_URL` to the job site you want to monitor
   - Customize `KEYWORDS` to match your job search
   - Update `JOB_ELEMENT_TAG` and `JOB_ELEMENT_CLASS` based on the website's HTML structure

5. **Run the bot**:
   ```bash
   python bot.py
   ```

## Configuration

Edit these variables in `bot.py`:

```python
TARGET_URL = "https://realpython.github.io/fake-jobs/"  # Website to scrape
JOB_ELEMENT_TAG = "h2"                                   # HTML tag containing job titles
JOB_ELEMENT_CLASS = "title"                              # CSS class name
KEYWORDS = ["python", "developer", "engineer"]           # Search keywords
DISCORD_WEBHOOK_URL = "YOUR_WEBHOOK_URL"                 # Discord notification URL
```

## How It Works

1. **Fetch**: Downloads the job website using HTTP requests
2. **Parse**: BeautifulSoup organizes the HTML into a searchable structure
3. **Extract**: Finds all job titles based on your configured selectors
4. **Filter**: Checks if any keywords match the job title
5. **Notify**: Sends a Discord message with matching job details
6. **Schedule**: Repeats at your configured interval


## License

MIT License - Feel free to use this project for personal or commercial purposes.

## Author

Created as a learning project for web scraping, automation, and API integration.

