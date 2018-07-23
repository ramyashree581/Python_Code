import requests

url = "https://api.github.com/user"

headers = {
    'authorization': "Basic cmFteWFzaHJlZTU4MToxODExM3lhQHNocmVl",
    'cache-control': "no-cache",
    'postman-token': "dde16c0b-ef78-631f-acf1-564c6f2af96d"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)