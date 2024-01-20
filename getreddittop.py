import praw
import datetime as dt
import toml



def reddittop(subreddit):

    with open('config.toml', 'r') as f:
        config = toml.load(f)

    reddit_api = praw.Reddit(
        client_id=config['redditlogin']['client_id'],
        client_secret=config['redditlogin']['client_secret'],
        user_agent=config['redditlogin']['user_agent'],
        username=config['redditlogin']['username'],
        password=config['redditlogin']['password'],
    )
    
    topics_dict = {
        "title": [],
        "body": [],
        "ID": [],
    }
    try:
        submission = next(x for x in reddit_api.subreddit(subreddit).hot() if not x.stickied)
        print(submission)
        print(submission.selftext)
        topics_dict["title"].append(submission.title)
        topics_dict["body"].append(submission.selftext)
        topics_dict["ID"].append(submission.id)
        return submission.title,submission.selftext,submission.id
    except Exception as e:
        print("error")
        print(e)