import requests
import json

import time
import hmac
import hashlib
import base64
import urllib.parse

timestamp = str(round(time.time() * 1000))
secret = '' #SEC开头的
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)

# 钉钉机器人Webhook URL
token = '' #webhook access_token
webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token='+token+'&sign='+sign+'&timestamp='+timestamp

def send_message(content, at_mobiles=[]):
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "atMobiles": at_mobiles,  # 填入需要@的用户手机号
            "isAtAll": False  # 是否@所有人
        }
    }

    response = requests.post(webhook_url, headers=headers, data=json.dumps(data))
    return response.json()

def handle_message(message):
    # 检查消息内容
    if '@信息科' in message:  # 替换为你的机器人的名称
        # 需要@的用户手机号列表
        at_mobiles = [""]  # 填入需要提醒的用户手机号，如["13800000000", "13900000000"]
        send_message("机器人被@了，相关用户被提醒！", at_mobiles)

# 测试示例：模拟接收到消息并处理
incoming_message = "大家好，@用户组名称 请注意项目进展！"  #模拟的消息
handle_message(incoming_message)