import requests
import json
import id
import switchbot_sign


# 認証ヘッダー作成
token = id.token
secret = id.secret

devices_url = "https://api.switch-bot.com/v1.1/devices"
headers = switchbot_sign.make_header(token, secret)
print(headers)

# GET
res = requests.get(devices_url, headers=headers)

# 出力内容を整形
json_data = res.json()
s = json.dumps(json_data, indent=2, ensure_ascii=False)
print(s)