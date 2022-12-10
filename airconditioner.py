import requests
import json
import sys
import id
import switchbot_sign



def main():

    device_id = id.airconditioner
    headers = switchbot_sign.make_header(id.token, id.secret)
    url = "https://api.switch-bot.com/v1.1/devices/" + device_id + "/commands"

    try:
        mode = sys.argv[1]
    except:
        print("Argument Error: Should Enter Argument;")
        print("    1st arg... h:hot / c:cold / d:dry / 0:off")
        print("    2nd arg... temperature (if turn off then type \"0\")")
        print("    $ python airconditioner.py h 21  <-example")
        exit()

    if mode=="h" or mode=="c" or mode=="d":
        body = make_body_turnon(mode)
    elif mode=="0":
        body = make_body_turnoff()

    send_requests(url, headers, body)



# エアコンをつける場合のbody作成
def make_body_turnon(mode):
    if mode == "h":
        mode = "5"
    elif mode == "c":
        mode = "2"
    elif mode == "d":
        mode = "3"
    else:
        print("Argument Error: Should Enter Argument;")
        print("    1st arg... h:hot / c:cold / d:dry / 0:off")
        print("    2nd arg... temperature (if turn off then type \"0\")")
        print("    $ python airconditioner.py h 21  <-example")
        exit()

    # 温度取得
    temperature = sys.argv[2]

    # パラメータ作成
    parameter = temperature+","+mode+",1,on"

    # 要求データ作成
    body={
        "command": "setAll",
        "parameter": parameter,
        "commandType": "command"
        }
    return body



#  エアコンを消す場合のbody作成
def make_body_turnoff():
    body={
        "command":"setAll",
        "parameter":"0,0,0,off",
        "commandType":"command"
    }
    return body



# bodyを送って結果を表示
def send_requests(url, headers, body):
    # POST
    r = requests.post(url, headers=headers, data=json.dumps(body))

    # 出力内容整形
    json_data = r.json() 
    s = json.dumps(json_data, indent=2, ensure_ascii=False)
    print(s)



if __name__ == "__main__":
    main()