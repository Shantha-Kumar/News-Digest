import requests

url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-10-22&sort"
       "By=publishedAt&apiKey=32c5b4044e104bbea4ab5ef9aad12496")

# Make request
request = requests.get(url)

# Get a dictionary
content = request.json()


for article in content['articles']:
    print(article['source'])


