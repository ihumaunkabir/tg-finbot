import json
import requests
from config import APIURL, AUTH, DATAPOINT, VLLM, PROJECTID


def handle_resp(text: str) -> str:
    text = text.lower()
    if 'hello' in text:
        return 'Hello'
    elif 'bangladesh' in text:
        return 'Bangladesh is a south asian country.'
    else:
        return 'I do not understand.'
    
def handle_file(path):
        print(path)
        # http = urllib3.PoolManager()
        # url = "https://official-joke-api.appspot.com/random_joke"
        # response = urlopen(url)
        # string = response.read().decode('utf-8')
        # json_obj = json.loads(string)
        # resptext = "Jokes: " + json_obj['punchline'] + "\n" + "Type: " + json_obj['type'] + " "

        respurl = requests.post(APIURL, headers={"Content-Type":"application/json","Authorization": AUTH}, data=json.dumps({"params":{"file_url": path,"data_points": DATAPOINT,"llm_choice":VLLM},"project": PROJECTID}))
        print(respurl.text)
        json_obj = json.loads(respurl.text)
        resptext = json_obj['output']['data']

        return resptext