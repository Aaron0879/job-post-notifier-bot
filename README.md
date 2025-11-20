# Job Post Notifier Bot

A Python-based automation bot that scrapes job portals for role-specific keywords and sends real-time notifications via Discord Webhooks.

## Features

✨ **Automated Job Scraping**: Continuously monitors job websites for new postings
🔍 **Keyword Filtering**: Search for specific job titles, skills, or keywords
🔔 **Discord Notifications**: Get instant alerts when matching jobs are found
⏰ **Customizable Schedule**: Run checks at intervals (every minute, hourly, daily, etc.)
🛡️ **Error Handling**: Gracefully handles network failures and timeouts
⚙️ **Easy Configuration**: Simple config section for URLs, selectors, and keywords

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

## Finding HTML Selectors for Real Websites

To scrape a real job website:

1. Open the website in your browser
2. Right-click on a job title → **Inspect**
3. Look at the HTML code:
   - Find the tag: `<h2>`, `<h3>`, `<a>`, etc.
   - Find the class: `class="job-title"`, `class="position"`, etc.
4. Update `JOB_ELEMENT_TAG` and `JOB_ELEMENT_CLASS` in your code

**Example**:
```html
<!-- If the HTML looks like: -->
<h3 class="job-heading">Senior Python Developer</h3>

<!-- Update your config to: -->
JOB_ELEMENT_TAG = "h3"
JOB_ELEMENT_CLASS = "job-heading"
```

## Example Schedule Options

```python
# Every 1 minute (testing)
schedule.every(1).minutes.do(check_jobs)

# Every 30 minutes
schedule.every(30).minutes.do(check_jobs)

# Every hour
schedule.every().hour.do(check_jobs)

# Every day at 9:00 AM
schedule.every().day.at("09:00").do(check_jobs)
```

## Future Enhancements

- 📊 Database to track applied jobs and avoid duplicate alerts
- 📧 Email notifications as alternative to Discord
- 🌐 Web dashboard to manage the bot
- 🔐 Environment variables for sensitive configuration
- 🧠 Machine learning to rank jobs by relevance
- 📱 Mobile app integration

## Troubleshooting

### Bot doesn't send Discord notifications
- **Check**: Verify your Webhook URL is correct and still active
- **Check**: Ensure you have internet connection
- **Check**: Discord Webhook might have expired (create a new one)

### No jobs are being found
- **Check**: Verify the website structure hasn't changed
- **Check**: Right-click and inspect the job title again to confirm selectors
- **Check**: Try testing with the fake jobs site first: `https://realpython.github.io/fake-jobs/`

### Script crashes with timeout error
- The error is caught and logged. The script will continue running and retry on the next check.

## Resume Description

**Job Market Automated Scraper**

Designed and deployed a Python-based automation bot utilizing BeautifulSoup for HTML parsing and the Requests library for HTTP communication to scrape career portals for role-specific keywords. Integrated Discord Webhooks API to deliver real-time push notifications when target opportunities are identified, reducing manual job search time. Implemented job scheduling logic using the Schedule library to execute scraping tasks at configurable intervals. Developed robust error handling with try-except blocks and timeouts to gracefully manage network failures, ensuring reliable bot operation.

## License

MIT License - Feel free to use this project for personal or commercial purposes.

## Author

Created as a learning project for web scraping, automation, and API integration.

---

Happy job hunting! 🎯
