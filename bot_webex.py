from flask import Flask, request
import requests
app = Flask(__name__)
botEmail = "mVillage_health_care@webex.bot"#bot's email address
accessToken = "MWM3NGVlYTItZDYzOC00ODU2LWIzZDctMGM1MTQxOTcyNzY0N2MxNmViMWYtY2Iw_PF84_fd330d04-8403-40ae-b798-40d0587e01bb" #Bot's access token
host = "https://api.ciscospark.com/v1/"#end point provided by the CISCO Spark to communicate between their services
server = "localhost" #Web hook won't work until the server sets up
port = 4000
headers = {"Authorization": "Bearer %s" % accessToken,"Content-Type": "application/json"}
token = 'Bearer '
@app.route('/test', methods=['POST','GET'])
def get_tasks():
    return "Hello"
@app.route('/', methods=['POST'])
def get_message():
    messageId = request.json.get('data').get('id')
    messageDetails = requests.get(host+"messages/"+messageId, headers = headers)
    responseMessage = messageDetails.json().get('text')
    print(responseMessage)
    return "Under construction NAJA!!!"
if __name__ == '__main__':
        app.run(host='0.0.0.0',port=80)