import requests
from bs4 import BeautifulSoup
import schedule
import time
import datetime
import json
import os

TARGET_URL = "https://realpython.github.io/fake-jobs/" 

JOB_ELEMENT_TAG = "h2" 
JOB_ELEMENT_CLASS = "title"

DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL_HERE"

KEYWORDS = ["python", "developer", "engineer"]

# File to store jobs we've already seen
SEEN_JOBS_FILE = "seen_jobs.json"

def load_seen_jobs():
    """Load the list of jobs we've already alerted about."""
    if os.path.exists(SEEN_JOBS_FILE):
        with open(SEEN_JOBS_FILE, "r") as f:
            return json.load(f)
    return []

def save_seen_jobs(jobs):
    """Save the list of seen jobs to avoid duplicate alerts."""
    with open(SEEN_JOBS_FILE, "w") as f:
        json.dump(jobs, f, indent=2)

def send_discord_alert(job_title, job_link):

    data = {
        "content": f"🚨 **Job Found!**\n**Role:** {job_title}\n**Link:** {job_link}"
    }
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=data, timeout=5)
        print(f"Notification sent for: {job_title}")
    except requests.exceptions.Timeout:
        print(f"Discord notification timeout for: {job_title} (will retry next check)")
    except requests.exceptions.ConnectionError:
        print(f"Discord connection error for: {job_title} (check your internet)")
    except Exception as e:
        print(f"Error sending Discord alert: {e}")

def check_jobs():
    print(f"Checking for jobs at {datetime.datetime.now().strftime('%H:%M:%S')}...")
    
    try:
        response = requests.get(TARGET_URL)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Load previously seen jobs
        seen_jobs = load_seen_jobs()

        jobs = soup.find_all(JOB_ELEMENT_TAG, class_=JOB_ELEMENT_CLASS)
        
        found_count = 0
        for job in jobs:
            title = job.text.strip()
            title_lower = title.lower()
            
            # Check if any of your keywords are in the job title
            if any(keyword in title_lower for keyword in KEYWORDS):
                
                # Check if we've already alerted about this job
                if title not in seen_jobs:
                    print(f"Match found: {title}")
                    if DISCORD_WEBHOOK_URL != "YOUR_DISCORD_WEBHOOK_URL_HERE":
                        send_discord_alert(title, TARGET_URL)
                    else:
                        print("  -> Discord Webhook URL not set. Skipping notification.")
                    
                    # Add to seen jobs
                    seen_jobs.append(title)
                    found_count += 1
                else:
                    print(f"Already notified: {title} (skipping duplicate)")
                
        # Save updated list of seen jobs
        save_seen_jobs(seen_jobs)
        
        if found_count == 0:
            print("No new matching jobs found this time.")
            
    except Exception as e:
        print(f"Error scraping: {e}")


schedule.every(1).minutes.do(check_jobs) 

print("Bot started! Press Ctrl+C to stop.")
check_jobs() 

while True:
    schedule.run_pending()
    time.sleep(1)
