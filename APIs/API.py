from flask import Flask, request, jsonify
import boto3
import io

# Initialize S3 and Rekognition clients with the specified region
s3_client = boto3.client('s3', region_name='us-east-1')  # Replace with your desired region
rekognition_client = boto3.client('rekognition', region_name='us-east-1')

app = Flask(__name__)

def get_image_from_s3(bucket_name, object_key):
    # Retrieve image from S3 bucket
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    image_content = response['Body'].read()
    return image_content

def detect_inappropriate_content(image_bytes):
    # Call Rekognition to detect moderation labels
    response = rekognition_client.detect_moderation_labels(
        Image={'Bytes': image_bytes},
        MinConfidence=70  # Set confidence threshold (optional)
    )
    return response['ModerationLabels']

@app.route('/check-image', methods=['POST'])
def check_image():
    # Get bucket name and object key from request JSON
    data = request.json
    bucket_name = data.get('bucket_name')
    object_key = data.get('object_key')

    if not bucket_name or not object_key:
        return jsonify({'error': 'Missing bucket_name or object_key'}), 400

    try:
        # Retrieve image from S3
        image_bytes = get_image_from_s3(bucket_name, object_key)

        # Detect inappropriate content using Rekognition
        moderation_labels = detect_inappropriate_content(image_bytes)

        if moderation_labels:
            return jsonify({
                'inappropriate_content_detected': True
            })
        else:
            return jsonify({
                'inappropriate_content_detected': False
            })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
