import praw
import datetime as dt

reddit = praw.Reddit(
    client_id="WG3ezIr2eqgmLLyZEFTEKA",
    client_secret="jaUS5N0VkStEm0zBNKGBvZW29ICdEA",
    user_agent="test",
    username="teamtijmi",
    password="@Thijmen18",
)


def reddittop(subreddit):
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
