# Load environment variables
from dotenv import load_dotenv
import os
load_dotenv()

from flask import Flask, request
import requests
import json

search_url = os.getenv("QUERY_SERVICE")

app = Flask("frontend-flask")
app.config["DEBUG"] = True

# Main page
@app.route("/", methods=["GET"])
def homepage():
    return app.send_static_file("index.html")

# Health Check
@app.route("/health", methods=["GET"])
def health():
    return {"status": "UP"}

# Handle form submission
@app.route('/startSearch', methods=['POST'])
def start_search():
    search_string = request.form['search']
    
    headers={'Content-type':'application/json'}
    payload= json.dumps({ "query": search_string })

    print("searching for the following string:",search_string)
    response = requests.request("POST", search_url, headers=headers, data=payload)
    
    print(response.text)
    
    results = json.dumps(response.text, indent=2)

    # END OF CODE FROM JUPYTER
    return "<h1>RESULTS:</h1><p>" + results + "</p><br/><a href=\"/\">Go Back</a>"

app.run(host='0.0.0.0', port=8080, threaded=True)