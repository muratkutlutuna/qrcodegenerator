import requests
from bs4 import BeautifulSoup
import subprocess
from datetime import datetime

# Step 1: Scrape the Akşam Namaz Time from the Website
url = 'https://namazvakitleri.diyanet.gov.tr/tr-TR/14543/winterthur-icin-namaz-vakti'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract Akşam Namaz time
prayer_times_row = soup.find('div', id='today-pray-times-row')
aksam_time = prayer_times_row.find('div', {'data-vakit-name': 'aksam'}).find('div', class_='tpt-time').text.strip()

# Convert Akşam time to 24-hour format (assuming the time format is HH:MM)
aksam_datetime = datetime.strptime(aksam_time, "%H:%M")
aksam_time_str = aksam_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Step 2: AppleScript to Create Calendar Event
apple_script = f'''
tell application "Calendar"
    set newEvent to make new event at calendar "Home" with properties {{summary:"Akşam Namaz Vakti", start date:date "{aksam_time_str}", end date:date "{aksam_time_str}"}}
    tell newEvent
        make new display alarm at end of display alarms with properties {{trigger interval:-5}}
    end tell
end tell
'''

# Step 3: Execute the AppleScript via osascript using subprocess
subprocess.run(['osascript', '-e', apple_script])

print(f"Event 'Akşam Namaz Vakti' scheduled at {aksam_time_str}")
