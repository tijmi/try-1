import praw
import datetime as dt
import toml
import prawcore.exceptions as prerror
from prawcore import NotFound
import prawcore.exceptions as prerror
from prawcore import NotFound



def sub_exists(subreddit) -> bool:
    with open("config.toml", "r") as f:
        config = toml.load(f)
    
    reddit_api = praw.Reddit(
        client_id= config["redditlogin"]["client_id"],
        client_secret=config["redditlogin"]["client_secret"],
        user_agent=config["redditlogin"]["user_agent"],
        username=config["redditlogin"]["username"],
        password=config["redditlogin"]["password"],
    )

    exists = True
    try:
        reddit_api.subreddits.search_by_name(subreddit, exact=True)
    except NotFound:
        exists = False
    return exists

def reddittop() -> tuple:
    with open("config.toml", "r") as f:
        config = toml.load(f)

    subreddit = config["preferances"]["subreddit"]

    reddit_api = praw.Reddit(
        client_id= config["redditlogin"]["client_id"],
        client_secret=config["redditlogin"]["client_secret"],
        user_agent=config["redditlogin"]["user_agent"],
        username=config["redditlogin"]["username"],
        password=config["redditlogin"]["password"],
    )

    try:
        print("getting reddit toppost")
        submission = next(
            x for x in reddit_api.subreddit(subreddit).hot() if not x.stickied
        )
        print(submission)
        print(submission.selftext)
        return submission.title, submission.selftext, submission.id
    except prerror.ResponseException:
        raise ValueError("Something went wrong during authentication")
    except prerror.RequestException:
        raise RuntimeError(
            "no internet conenction found, please connect to wifi or ethernet"
        )
