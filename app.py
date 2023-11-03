from flask import Flask

app = Flask(__name__)

@app.route('/trigger-cloud-function', methods=['GET'])
def trigger_cloud_function():
    import requests
    cloud_function_url = 'https://us-central1-docai-335206.cloudfunctions.net/threewaymatch-new'

    response = requests.get(cloud_function_url)

    return f'Cloud Function Response: {response.text}'
