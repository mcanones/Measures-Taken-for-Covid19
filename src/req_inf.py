import requests
import json

def request_inf(path):
    url = f"https://corona-api.com/countries/{path}?include=timeline"
    res = requests.get(url)
    print(res.status_code, res.url)
    return res.json()