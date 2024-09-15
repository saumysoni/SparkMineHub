from flask import Flask, request, jsonify
from profanity import profanity

app = Flask(__name__)

@app.route('/check-profanity', methods=['POST'])
def check_profanity():
    # Get text from request JSON
    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({'error': 'Missing text field'}), 400

    # Check if the text contains profanity
    contains_profanity = profanity.contains_profanity(text)
    
    return jsonify({
        'contains_profanity': contains_profanity
    })

@app.route('/censor-text', methods=['POST'])
def censor_text():
    # Get text from request JSON
    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({'error': 'Missing text field'}), 400

    # Censor the text
    censored_text = profanity.censor(text)
    
    return jsonify({
        'censored_text': censored_text
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=False)
