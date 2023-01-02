import requests
import json
import sys
import id
import switchbot_sign
import execute_scene


# 引数エラーメッセージ
error_arg_message = "Argument Error: Should Enter Argument\n" \
                    "    python light.py 0    <- Off\n" \
                    "    python light.py 1    <- On(Blight)\n" \
                    "    python light.py d    <- On(Dark)\n" \
                    "    python light.py n    <- On(Nightlight)\n" \

# ヘッダー作成
device_id = id.light
headers = switchbot_sign.make_header(id.token, id.secret)
url = "https://api.switch-bot.com/v1.1/devices/" + device_id + "/commands"



try:
    mode = sys.argv[1]
except:
    print(error_arg_message)
    exit()



# 要求データ作成
# 0=OFF  1=ON(明)  d=ON(暗)  n=常夜灯

if mode == "0":
    body={
    "command": "turnOff",
    "parameter": "default",
    "commandType": "command"
    }

elif mode == "1":
    body={
        "command": "turnOn",
        "parameter": "default",
        "commandType": "command"
        }

elif mode == "d":
    execute_scene.main(id.scene_darklight)
    exit()

elif mode ==  "n":
    execute_scene.main(id.scene_nightlight)
    exit()

else:
    print(error_arg_message)
    exit()



# POST
r = requests.post(url, headers=headers, data=json.dumps(body))

# 出力内容整形
json_data = r.json() 
s = json.dumps(json_data, indent=2, ensure_ascii=False)
print(s)
