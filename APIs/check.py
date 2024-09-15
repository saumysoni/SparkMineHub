import requests

# URL of the Flask API endpoint
api_url = 'http://127.0.0.1:8080/check-image'

# Data to be sent in the POST request
data = {
    'bucket_name': 'inappropriatebucket',  # Replace with your S3 bucket name
    'object_key': 'folder1/R.jpeg'          # Replace with your S3 object key
}

# Make the POST request to the Flask API
response = requests.post(api_url, json=data)

# Print the response from the API
print(f"Status Code: {response.status_code}")
print("Response JSON:", response.json())
