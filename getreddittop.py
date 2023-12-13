import praw
import datetime as dt
import toml



def reddittop(subreddit):

    with open('config.toml', 'r') as f:
        config = toml.load(f)

    reddit = praw.Reddit(
        client_id=config['reddit']['client_id'],
        client_secret=config['reddit']['client_secret'],
        user_agent=config['reddit']['user_agent'],
        username=config['reddit']['username'],
        password=config['reddit']['password'],
    )
    
    topics_dict = {
        "title": [],
        "body": [],
        "ID": [],
    }

    submission = next(x for x in reddit.subreddit(subreddit).hot() if not x.stickied)
    topics_dict["title"].append(submission.title)
    topics_dict["body"].append(submission.selftext)
    topics_dict["ID"].append(submission.id)
    return submission.title,submission.selftext,submission.id
