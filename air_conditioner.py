import requests
import json
import sys
import id
import switchbot_sign


# ヘッダー作成
device_id = id.airconditioner
headers = switchbot_sign.make_header(id.token, id.secret)


# 引数取得
try:
    mode = sys.argv[1]
    temperature = sys.argv[2]

except:
    print("Argument Error: Should Enter Argument;")
    print("    1st arg... h:hot / c:cold / d:dry / 0:off")
    print("    2nd arg... temperature (if turn off then type \"0\")")
    print("    $ python airconditioner.py h 21  <-example")
    exit()


# mode変換( hot→5 / cold→2 / dry→3 )
if mode == "h":
    mode = "5"
elif mode == "c":
    mode = "2"
elif mode == "d":
    mode = "3"
elif mode == "0":
    mode = "0"
else:
    print("Argument Error: Should Enter Argument;")
    print("    1st arg... h:hot / c:cold / d:dry / 0:off")
    print("    2nd arg... temperature (if turn off then type \"0\")")
    print("    $ python airconditioner.py h 21  <-example")
    exit()


# パラメータ作成
parameter = temperature+","+mode+",1,on"


# 要求データ作成
url = "https://api.switch-bot.com/v1.1/devices/" + device_id + "/commands"
body = {}

if mode=="2" or mode=="3" or mode=="5":
    body={
        "command": "setAll",
        "parameter": parameter,
        "commandType": "command"
        }

if mode=="0":
    body={
        "command":"setAll",
        "parameter":"0,0,0,off",
        "commandType":"command"
    }


# POST
r = requests.post(url, headers=headers, data=json.dumps(body))


# 出力内容整形
json_data = r.json() 
s = json.dumps(json_data, indent=2, ensure_ascii=False)
print(s)