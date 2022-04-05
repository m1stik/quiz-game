import requests

# Parameters for the further API request
params = {
    "amount": 10,
    "type": "boolean"
}

# Getting data from the API
response = requests.get("https://opentdb.com/api.php", params=params)
response.raise_for_status()

# Store the data
data = response.json()
question_data = data["results"]