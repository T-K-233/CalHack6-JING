import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=1cfb1a00469d4ff79630775d5b0c657d')
response = requests.get(url)
print(response.json())
