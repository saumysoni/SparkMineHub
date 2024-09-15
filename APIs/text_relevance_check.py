import requests

# URL of the Flask API
url = 'http://127.0.0.1:8082/classify'

# Sample text to classify
data = {
    'text': 'Mining is a critical industry for the economy. It involves the extraction of valuable minerals from the earth.'
}

# Send a POST request to the API
response = requests.post(url, json=data)

# Print the response from the API
print('Status Code:', response.status_code)
print('Response JSON:', response.json())
