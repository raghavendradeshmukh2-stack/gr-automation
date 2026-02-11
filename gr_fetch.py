import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, db
import os
import json
# Firebase Setup
firebase_key = json.loads(os.environ["FIREBASE_KEY"])
cred = credentials.Certificate(firebase_key)
firebase_admin.initialize_app(cred, {'databaseURL':"https://dynamic-gr-150b5-default-rtdb.asia-southeast1.firebasedatabase.app/"})
url = "https://gr.maharashtra.gov.in/1145/Government-Resolutions"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
gr_list = []
for item in soup.select("table tr"):
    text = item.get_text(strip=True)
    if text:
        gr_list.append(text)
ref = db.reference("gr_data")
ref.set(gr_list)
print("GR Data Updated Successfully")
