import requests
import json
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-summary"

querystring = {"region":"US","lang":"en"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "6e2f59b824mshcf452fa0ba63c97p12c62djsn5045e8c330ad"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
with open ('request.json', 'w', encoding='utf-8') as text:
    json.dump(data, text)