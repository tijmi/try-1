import praw
import datetime as dt
import toml
import prawcore.exceptions as prerror
from prawcore import NotFound


class reddit:
    def __init__(self) -> None:

        with open("config.toml", "r") as f:
            config = toml.load(f)

        self.subreddit = config["preferances"]["subreddit"]

        self.client_id = config["redditlogin"]["client_id"]
        self.client_secret = config["redditlogin"]["client_secret"]
        self.user_agent = config["redditlogin"]["user_agent"]
        self.username = config["redditlogin"]["username"]
        self.password = config["redditlogin"]["password"]

    def sub_exists(self) -> bool:
        exists = True
        try:
            praw.search_by_name(self.subreddit, exact=True)
        except NotFound:
            exists = False
        return exists

    def reddittop(self) -> tuple:

        reddit_api = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
            username=self.username,
            password=self.password,
        )

        try:
            print("getting reddit toppost")
            submission = next(
                x for x in reddit_api.subreddit(self.subreddit).hot() if not x.stickied
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
