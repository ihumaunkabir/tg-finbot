import json
import requests
from config.config import APIURL, VLLM, BEARER

def handle_resp(text: str) -> str:
    headers = {"Authorization": BEARER}
    respurl = requests.post(APIURL, timeout=120,headers=headers, data=json.dumps({"stream":False,"prompt": text,"model":VLLM, "temperature":0.4}))
    # print(f'API response is: {respurl.text}')
    json_obj = json.loads(respurl.text)
    resptext = json_obj['response']

    print(respurl.status_code)
    if respurl.status_code == 200:
         return resptext
    else:
          return 'Unfortunately I am offline, thanks you.'

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