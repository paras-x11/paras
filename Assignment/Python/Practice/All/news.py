import requests
import json 

query = input("What type of news are you interested in? ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2024-11-05&sortBy=publishedAt&apiKey=56e818fd8692475f9f7ab618adca50cc"

# Send the request and check if the response is successful
try:
    r = requests.get(url)
    r.raise_for_status()  # Will raise an exception for 4xx/5xx responses

    news = r.json()

    # Iterate through the articles if the API returned articles
    if news.get("articles"):
        for articles in news["articles"]:
            print(articles["title"])
            print(articles["description"])
            print("--------------------------------------")
    else:
        print("No articles found for this query.")
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
