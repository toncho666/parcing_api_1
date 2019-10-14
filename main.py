import requests
import json
main_link = 'https://api.github.com/users/'
user = input('Укажите имя пользователя: ')
req = requests.get(main_link+user+'/repos')

data = json.loads(req.text)


i = 0
rep_list = []
while i < len(data):
    rep_list.append(data[i]['url'])
    i = i+1

with open ('data.json', 'w', encoding='utf-8') as f:
    json.dump(rep_list, f)