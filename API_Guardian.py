import requests
import json
from datetime import datetime, timedelta
from keys import guardian_key

api_key = guardian_key

# Set up the API endpoint
endpoint = 'https://content.guardianapis.com/search'
def get_last_seven_days():
    current_date_str = datetime.now().strftime('%Y-%m-%d')
    seven_days_ago_str = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    return seven_days_ago_str, current_date_str

# Calls the function assigning the values in variables
seven_days_ago_str, current_date_str = get_last_seven_days()

# Define the parameters for the request
params = {
    'q': '"knife" OR "blade" OR "stab" OR "stabbing" OR "stabbed"' ,  # Search for the keyword 'knife crime'
    'section': 'uk-news',  # Specify the section for UK news
    'from-date': seven_days_ago_str,  # Optional: Set the start date for the articles
    'to-date': current_date_str,  # Optional: Set the end date for the articles
    'api-key': api_key,  # Your API key
    'page-size': 100,  # Optional: Number of results per page (can adjust as needed)
    #'order-by': 'relevance',  # Optional: Order results by relevance
    'show-fields': 'headline,webPublicationDate,shortUrl,body'  # Optional: Fields to include in the response
}

# Request to The Guardian API
def fetch_guardian():
    response = requests.get(endpoint, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the response JSON
        results = data.get('response', {}).get('results', [])
        
        # Create a list to store the fetched articles
        articles = []

        # Append each article's details to the list
        for article in results:
            article_data = {
                'API':'Guardian',
                'published_at': article['webPublicationDate'],
                'title': article['webTitle'],
                # 'body': article['fields'].get('body', 'No body content available'),
                'url': article['webUrl']
            }
            articles.append(article_data)
        #print(articles)
        return articles  # Return the list of articles

    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []  # Return an empty list in case of failure
if __name__ == '__main__':
    fetch_guardian()