import requests

api_url = "https://api.openweathermap.org/data/2.5/weather"
params={
    'q':"Moscow",
    'appid':'aefc3ebd56880db3ed48a1fd0462cb28',
    "units":"metric"
}
res=requests.get(api_url,params)
data=res.json()
temp=data['main']['temp']
print(temp)