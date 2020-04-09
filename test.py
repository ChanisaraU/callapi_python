from flask import Flask, request, abort
import requests
import json

Channel_access_token = 'Yytu/+0UOeK6Wgu9Hk5Yikvgtw4hNpSRc4e93WFPckljMll+7/ne/5KUgSCY7/Nf5/+VQQVL48ElnmFbYEbm8C805tphw+6L+2lct/lxU/mVxnsL0hSLVnCZXo0Y+ULakDfKBwvMyrhA2Olj7dvqdgdB04t89/1O/w1cDnyilFU='
app = Flask(__name__)

def GET_BTC_PRICE():
    data = requests.get('https://bx.in.th/api/')
    BTC_PRICE = data.text.split('BTC')[1].split('last_price":')[1].split(',"volume_24hours')[0]
    return BTC_PRICE

def COVID_TODAY():
    data = requests.get('https://covid19.th-stat.com/api/open/today')
    json_data = json.loads(data.text)
    covid = json_data['Confirmed']
    return covid

@app.route('/webhook', methods=['POST','GET'])
def webhook():
        if request.method == 'POST':
            payload = request.json
            print(payload)
            Reply_token = payload['events'][0]['replyToken']
            print(Reply_token)
            message = payload['events'][0]['message']['text']
            print(message)
            if "btc" in message :
                Reply_messasge = 'ราคา BITCOIN ขณะนี้ : {}'.format(GET_BTC_PRICE())
                ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
            
            elif "โควิด" in message :
                Reply_messasge = 'ผู้ป่วยสะสมวันนี้ของโควิด: {}'.format(COVID_TODAY())
                ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
            
            return request.json, 200

        elif request.method == 'GET' :
            return 'this is method GET!!!' , 200
            

        else:
            abort(400)



@app.route('/')
def hello():
    return 'get 443',200

def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) 
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        }]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200

if __name__ == '__main__':
    app.run(port=80)   
    # ssl_context=('cert.pem', 'key.pem')