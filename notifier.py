import requests
import urllib

# Send out messages to telegram

class Notifier:

    def __init__(self, botID, chatID):
        
        self._botID = botID
        self._chatID = chatID

    def message(self, text):
        print(urllib.quote(text))
        notifier = requests.get('https://api.telegram.org/' + self._botID + '/sendMessage?chat_id=' + self._chatID + '&text=' + urllib.quote(text))
        return