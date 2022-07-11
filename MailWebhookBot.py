import feedparser
import time
import re
import requests
url = " "
patternType = r"\bMord|RECKONING|Gargoyle|Sahn|Uzal|AP Bruiser|Rylai|Mitna|Rachnun|Death's Grasp|Stoneplate|Juggernaut|Mih|Aatrox|Nightfall|Riftmaker|Sunfire|Cooking|Mama|Abyssal"
lastDateStanding = "DEEZ NUTS"
while True:
    try:
        txt = feedparser.parse("https://www.reddit.com/user/theironkaiser/.rss")
        data = {
            'content': "Kaiser just posted cringe!\n<"+txt.entries[0].link+">",
            "username": "●●|●●●●●|●●|●"
                }
        print(lastDateStanding)
        print(txt.entries[0].date)
        if lastDateStanding != txt.entries[0].date:
            x = re.search(patternType, txt.entries[0].description, re.IGNORECASE)
            y = re.search(patternType, txt.entries[0].title, re.IGNORECASE)
            if x is not None or y is not None:
                requests.post(url, json=data)
                lastDateStanding = txt.entries[0].date
        time.sleep(15)
    except DeezNutsGottem:
        continue
