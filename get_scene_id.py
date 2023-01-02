import requests
import json
import id
import switchbot_sign



def main():

    headers = switchbot_sign.make_header(id.token, id.secret)
    url = "https://api.switch-bot.com/v1.1/scenes"

    r = requests.get(url , headers=headers)

    json_data = r.json() 
    s = json.dumps(json_data, indent=2, ensure_ascii=False)
    print(s)



if __name__ == "__main__":
    main()