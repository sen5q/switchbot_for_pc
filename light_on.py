import requests
import json
import id
import switchbot_sign

# ヘッダー作成
device_id = id.light
headers = switchbot_sign.make_header(id.token, id.secret)

# 要求データ作成
url = "https://api.switch-bot.com/v1.1/devices/" + device_id + "/commands"
body={
    "command": "turnOn",
    "parameter": "default",
    "commandType": "command"
    }

# POST
r = requests.post(url, headers=headers, data=json.dumps(body))

# 出力内容整形
json_data = r.json() 
s = json.dumps(json_data, indent=2, ensure_ascii=False)
print(s)