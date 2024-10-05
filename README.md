### tg-finbot

A telegram bot to receive texts, images or pdfs and answer questions accordingly using LLMs.

#### Installation
Install dependencies through pip
```
pip install -r requirements.txt
```

#### Configuring a Telegram bot
On Telegram hit to [@BotFather](https://t.me/BotFather) initiate your own bot and obtain ```BOT_TOKEN, BOT_USER```.

Example ```config/config.py``` with necessary keys and values.
```python
from typing import Final

BOT_TOKEN: Final = 'yourbottoken'
BOT_USER: Final = '@username'
APIURL: Final = 'llmapiendpoint'
VLLM: Final = 'mistral-nemo'
BEARER: Final = "Bearer bearertokenhere"
```

#### Backend
Run the backend of bot by
```
python main.py
```
Output
```
Bot started...
Bot polling...
```

#### Example Usage
Once your bot is running as well as your API is serving properly. Start interacting with your bot. 
