import requests
from bs4 import BeautifulSoup
import schedule
import time
import datetime

TARGET_URL = "https://realpython.github.io/fake-jobs/" 

JOB_ELEMENT_TAG = "h2" 
JOB_ELEMENT_CLASS = "title"


DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL_HERE"


KEYWORDS = ["python", "developer", "engineer"]

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
        

        jobs = soup.find_all(JOB_ELEMENT_TAG, class_=JOB_ELEMENT_CLASS)
        
        found_count = 0
        for job in jobs:
            title = job.text.strip().lower()
            
            if any(keyword in title for keyword in KEYWORDS):

                print(f"Match found: {job.text.strip()}")
                if DISCORD_WEBHOOK_URL != "YOUR_DISCORD_WEBHOOK_URL_HERE":
                    send_discord_alert(job.text.strip(), TARGET_URL)
                else:
                    print("  -> Discord Webhook URL not set. Skipping notification.")
                found_count += 1
                
        if found_count == 0:
            print("No matching jobs found this time.")
            
    except Exception as e:
        print(f"Error scraping: {e}")


schedule.every(1).minutes.do(check_jobs) 

print("Bot started! Press Ctrl+C to stop.")
check_jobs() 

while True:
    schedule.run_pending()
    time.sleep(1)
