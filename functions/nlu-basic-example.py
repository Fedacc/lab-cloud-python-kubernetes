#
#
# main() will be invoked when you Run This Action.
#
# @param Cloud Functions actions accept a single parameter,
#        which must be a JSON object.
#
# @return which must be a JSON object.
#         It will be the output of this action.
#
#
import sys
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions

# Authentication via external config like VCAP_SERVICES
natural_language_understanding = NaturalLanguageUnderstandingV1(version='2018-03-16')
natural_language_understanding.set_service_url('URL')
natural_language_understanding.set_iam_apikey('APIKEY')

def main(dict):
    
  response = natural_language_understanding.analyze(
      url='www.ibm.com',
      features=Features(categories=sentiment=SentimentOptions())).get_result()

  results = json.dumps(response, indent=2)
  
  return {'results':results}
