import requests

# URL of the Flask API endpoints
check_profanity_url = 'http://127.0.0.1:8081/check-profanity'
censor_text_url = 'http://127.0.0.1:8081/censor-text'

# Data to be sent in the POST request
data = {
    'text': 'Fuck You. You piece of shit'
}

# Test profanity check
response = requests.post(check_profanity_url, json=data)
print("Check Profanity Response:", response.json())

# Test text censoring
response = requests.post(censor_text_url, json=data)
print("Censor Text Response:", response.json())
