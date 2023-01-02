import requests
import json
import id
import switchbot_sign


# POST /v1.1/scenes/{sceneId}/execute


def main(scene_id):

    headers = switchbot_sign.make_header(id.token, id.secret)
    url = "https://api.switch-bot.com/v1.1/scenes/" + scene_id + "/execute"

    r = requests.post(url, headers=headers)

    json_data = r.json() 
    s = json.dumps(json_data, indent=2, ensure_ascii=False)
    print(s)


if __name__ == "__main__":
    main(id.sc_nightlight)