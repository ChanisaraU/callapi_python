import json
import os
import requests
from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():

    
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    # Parsing the POST request body into a dictionary for easy access.
    req_dict = json.loads(request.data)
    print(req_dict)
    # Accessing the fields on the POST request boduy of API.ai invocation of the webhook
    intent = req_dict["queryResult"]["intent"]["displayName"]

    if intent == 'callapipython':
        data = requests.get('https://covid19.th-stat.com/api/open/today')
        json_data = json.loads(data.text)
        covid = json_data['Confirmed']
        speech = covid

    else:

        speech = "ผมไม่เข้าใจ คุณต้องการอะไร"

    res = makeWebhookResult(speech)

    return res


def makeWebhookResult(speech):

    return {
        "fulfillmentText": speech
    }

if __name__ == '__main__':
    app.run(port= 5000)    