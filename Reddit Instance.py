import datetime
import praw
import psaw

reddit = praw.Reddit(
    client_id="lm46_WBhDlhpz7OKSJAWqQ",
    client_secret="yoUNr59xapFKlExtHcqiFnBE0ZJt0Q",
    user_agent="Shadow of kaiser bot, v0.1 by u/BasedOnDeezNuts and u/JustRevDice",
    username="ShadowOfKaiser",
    password="ReallyBased1",
)
subreddit = reddit.subreddit("leagueoflegends")
print(subreddit.display_name)
api = psaw.PushshiftAPI(reddit)
startTime = int(datetime.datetime(2021, 1, 1).timestamp())
gen = api.search_submissions(subreddit="leagueoflegends", limit=None, after=startTime, filter=['selftext'],)
results = list(gen)
filename = ""
File = open(filename, "a")
for i in range(len(results)):
    File.write(results[i].selftext)
    File.write("<|endoftext|>")
File.close()
