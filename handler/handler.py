import json
import requests
from config.config import APIURL, MODEL, SYSPROMPT

def handle_resp(text: str, last_text: str, last_resp: str) -> str:
    if last_text is None:
          last_text = ""
    if last_resp is None:
          last_resp = ""

#     headers = {"Authorization": BEARER}
    respurl = requests.post(APIURL, timeout=120, data=json.dumps({ "model": MODEL, "messages": [{"role": "system", "content": SYSPROMPT},{"role": "user", "content": last_text}, {"role": "assistant", "content": last_resp},{"role": "user","content": text}],"stream": False}))
    # print(f'API response is: {respurl.text}')
    json_obj = json.loads(respurl.text)
    resptext = json_obj['message']['content']

    print(respurl.status_code)
    if respurl.status_code == 200:
         return resptext
    else:
          return 'I am offline, try again later.'

def handle_file(path):
        print(path)
        # http = urllib3.PoolManager()
        # url = "https://official-joke-api.appspot.com/random_joke"
        # response = urlopen(url)
        # string = response.read().decode('utf-8')
        # json_obj = json.loads(string)
        # resptext = "Jokes: " + json_obj['punchline'] + "\n" + "Type: " + json_obj['type'] + " "

        # respurl = requests.post(APIURL, headers={"Content-Type":"application/json","Authorization": AUTH}, data=json.dumps({"params":{"file_url": path,"data_points": DATAPOINT,"llm_choice":VLLM},"project": PROJECTID}))
        # print(respurl.text)
        # json_obj = json.loads(respurl.text)
        # resptext = json_obj['output']['data']

        # return resptext