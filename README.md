# Intercom Article Export to CSV File 

Simple Python script for exporting Intercom articles to a csv file using the Intercom API.

Uses the following libraries:
- Requests
- Pandas

See requirements.txt for the complete list.

# Instructions:
1. Create an app and generate your API access token. 
    - Instructions found here: https://developers.intercom.com/building-apps/docs/authentication-types#section-access-tokens
2. Rename the file 'user_data_copy.json' to 'user_data.json'.
3. Add your API token and set the number of articles required. (Intercom default is 25)
4. cd into the 'src' folder and run 'python3 export.py'. A csv file called 'articles.csv' will be generated containing the data.
