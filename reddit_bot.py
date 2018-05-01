import praw, time
from pyshorteners import Shortener

def reddit():
    reddit = praw.Reddit('tilbot')
    subreddit = reddit.subreddit("todayilearned")
    for submission in subreddit.top('hour',limit=1):
        y = submission.title
        x = submission.permalink
    url = 'https://www.reddit.com/'+x
    shortener = Shortener('Tinyurl')
    tiny = shortener.short(url)
    tweet = y+' (from '+tiny+')'
    filename = "til.txt"
    file_variable = open(filename)
    j = file_variable.readlines()
    file_variable.close()
    outfile = open(filename,"w")
    for i in j:
        if i!=tweet:
            outfile.write(tweet)
    outfile.close()


while True:
    reddit()
    time.sleep(7200)