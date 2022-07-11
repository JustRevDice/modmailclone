import praw
import random
import time
reddit = praw.Reddit(
    client_id="UaK4A3wPEiJ3bpRWptKGZg",
    client_secret="VmOw0mDU300-F0iOWQWgbkrNwnjETA",
    user_agent="27 Bibles bot, v0.1 by u/BasedOnDeezNuts and u/JustRevDice",
    username="DevourerOf27Bibles01",
    password="BrasilKindaBased1",
)
submissions = reddit.redditor("JustRevDice").new()
pog = list(submissions)
replySubmission = reddit.submission(str(pog[0]))
time.sleep(600*random.random()+300)
#replySubmission.reply("Hi there!")
