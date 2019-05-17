#Проверяет, есть ли интересный факт про заданные числа из файла
import requests
with open("dataset_24476_3.txt") as f:
    for n in f.read().splitlines():
        type="/math"
        api_url = "http://numbersapi.com/"
        params={
            "json":"true"
        }
        res = requests.get(api_url+n+type,params)
        data = res.json()
        if data['found']:
            print("Interesting")
        else:
            print("Boring")
