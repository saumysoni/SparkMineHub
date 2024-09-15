from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

# Initialize the Comprehend client
comprehend = boto3.client('comprehend')

# Define the endpoint ARN
endpoint_arn = 'arn:aws:comprehend:us-east-1:364970310968:document-classifier-endpoint/Endpoint2'

@app.route('/classify', methods=['POST'])
def classify_text():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'Text is required'}), 400

    try:
        # Classify the text
        response = comprehend.classify_document(
            Text=text,
            EndpointArn=endpoint_arn
        )

        # Extract classification results
        classes = response['Classes']

        # Initialize variables to hold the scores
        mining_score = 0.0
        not_mining_score = 0.0

        # Process the classification results
        for classification in classes:
            if classification['Name'] == 'Mining':
                mining_score = classification['Score']
            elif classification['Name'] == 'Not Mining':
                not_mining_score = classification['Score']

        # Determine the final result
        result = mining_score > not_mining_score

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=False)
