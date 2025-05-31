"""
Email Extractor
Quickly extract email addresses from a webpage.

Usage:
1. Enter the target URL
2. Run the script to find all emails on the page
3. Save results for outreach or analysis

Tips:
- Some sites hide emails behind JavaScript or CAPTCHA
- Use responsibly and respect privacy policies
"""

import requests
import re
import time
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (compatible; EmailExtractor/1.0; +https://github.com/yourusername)'
}

def extract_emails(url, pause=2):
    print(f"Fetching page: {url}")
    time.sleep(pause)
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        emails = set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", response.text))
        print(f"Found {len(emails)} unique emails.")
        return list(emails)
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    target = "https://example.com"
    emails = extract_emails(target)
    print("Emails found:", emails)
