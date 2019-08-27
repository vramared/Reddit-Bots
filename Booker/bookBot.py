import praw
import config

def bot_login():
    log = praw.Reddit(username = config.username, 
                    password = config.password, 
                    client_id = config.client_id, 
                    client_secret = config.client_secret,
                    user_agent = "test")
    return log

def run_bot():
    for comment in log.subreddit("suns").comments(limit = 100):
        if "Booker" in comment.body:
            #print(comment.body)
            comment.reply("I see you have mentioned Devin Booker. [Here](https://imgur.com/gallery/yzNc0sH) is a picture of him.")


log = bot_login()
run_bot()
