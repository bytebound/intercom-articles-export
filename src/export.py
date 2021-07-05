import requests
import pandas as pd
import json

# Get the users api token and article count
user_data = open('user_data.json')
data = json.load(user_data)

token = data['token']
article_count = data['article_count']

url = "https://api.intercom.io/articles?per_page="+str(article_count)

# Set headers
headers = {
    "Authorization": "Bearer "+token,
    "Accept": "application/json"
}

# Send GET request and return response in .JSON
response = requests.get(url, headers=headers).json()

# Build Pandas dataframe using response data
df = pd.DataFrame(response['data'])

# Write data to .csv file
df.to_csv('articles.csv')