import requests
import json

client_id = 'f2bafb758b91c49d329a'
client_secret = 'e5ee2cc4910c763e2ad4b97ea54addf8'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]


# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком

dict_artists=[]
with open("dataset_24476_4.txt") as f:
    for artist_id in f.read().splitlines():
        r = requests.get("https://api.artsy.net/api/artists/"+artist_id, headers=headers)
        j = json.loads(r.text)
        dict_artists.append({'sortable_name':j['sortable_name'],"birthday":j["birthday"]})

    dict_artists.sort(key=lambda x:(x["birthday"], x['sortable_name']))
    for a in dict_artists:
        print(a["sortable_name"])