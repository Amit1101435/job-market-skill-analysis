import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {"User-Agent": "Mozilla/5.0"}
skills_keywords = ["SQL", "Python", "Power BI", "Excel", "Tableau", "R", "Azure", "AWS"]

job_listings = []

for page in range(0, 10):  # 10 pages
    url = f"https://www.indeed.com/jobs?q=data+analyst&start={page*10}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    
    for div in soup.find_all(name="div", attrs={"class":"job_seen_beacon"}):
        title = div.find("h2").text.strip()
        summary = div.find("div", class_="job-snippet").text.strip()
        job_listings.append({"title": title, "summary": summary})

    time.sleep(1)  # to avoid IP blocking

df = pd.DataFrame(job_listings)
df.to_csv("data/job_posts.csv", index=False)
print("Saved scraped data to CSV.")
