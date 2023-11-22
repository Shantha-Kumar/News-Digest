import requests
from send_mail import send_mail

topic = "tesla"
url = (f"https://newsapi.org/v2/everything?q={topic}&from=2023-10-22&sort"
       "By=publishedAt&apiKey=32c5b4044e104bbea4ab5ef9aad12496&language=en")

# Make request
request = requests.get(url)

# Get a dictionary
content = request.json()

body = "Subject: Today's News" \

for article in content['articles'][:10]:
    if article['title'] is not None:
        body = body + article['title'] + "\n" + article['description'] + "\n" + article['url'] + 2 * "\n"

body = body.encode("utf-8")
send_mail(body)
