import requests
import json


response=requests.get("https://www.reddit.com/r/learnpython/new.json",headers={"User-agent":"your bot 0.1"})
data=response.json()
print(data)