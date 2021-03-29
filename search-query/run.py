# Load environment variables
from dotenv import load_dotenv
import os
load_dotenv()

from flask import Flask, request, Response

# import IBM Watson SDK
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

# Authenticate with the service
authenticator = IAMAuthenticator(os.getenv("DISCOVERY_APIKEY"))
discovery = DiscoveryV1(
    version=os.getenv("DISCOVERY_VERSION"),
    authenticator=authenticator
)
discovery.set_service_url(os.getenv("DISCOVERY_URL"))

# Set up flask server
app = Flask("query-service")
app.config["DEBUG"] = True

# Expose endpoint for query
@app.route("/search",methods=["POST"])
def start_query():
    try:
        input_request = request.get_json()
        query = input_request['query']
        resp = {}
        if query is not None and len(query)>0:
            # Call Discovery
            discovery_response = discovery.query(
                environment_id = os.getenv("DISCOVERY_ENVIRONMENTID"),
                collection_id = os.getenv("DISCOVERY_COLLECTIONID"),
                natural_language_query = query
            ).get_result()
            # Manage payload of response from Discovery
            results = [] # empty list that will contain the simpler response 
            for result in discovery_response["results"]:
                answer = {
                    "text": result["text"],
                    "author": result["author"],
                    "url": result["url"],
                }
                results.append(answer)

            resp = Response(json.dumps({"results": results}), status=200, mimetype='application/json')

    except Exception as e:
        json_error_resp = json.dumps({"errorMessage": str(e)})
        resp = Response(json_error_resp, status=500, mimetype='application/json')

    return resp




app.run(host='0.0.0.0', port=3000, threaded=True)