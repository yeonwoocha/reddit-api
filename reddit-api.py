import praw
# from textblob import TextBlob
import csv
import json

# Reddit API 설정
reddit = praw.Reddit(
    client_id='NwNg7NRdXcASZMJcog3J0A',
    client_secret='G0kaD7Z_HI79QVc3Oz4GgVUGxthr-w',
    user_agent='ghskdneh99',
    username='ghskdneh99',
    password='ckdusdn44!'
)

subreddits = ['BitCoin'] # , 'stock'
keywords = ["buy", "good"]

data = []



def traverse_comments(comment, post_title, level=0):
    if level == 0:
        print(f'>> {post_title} \n' + "  " * level + f"ID: {comment.id}, Body: {comment.body}")
    else:
        print("  " * level + f"ID: {comment.id}, Body: {comment.body}")
    
    for reply in comment.replies:
        traverse_comments(reply, post_title, level+1)


for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    
    # Get the top 100 posts in the subreddit
    hot_posts = subreddit.hot(limit=2)
    for post in hot_posts:
        post.comments.replace_more(limit=None)
        post_title = post.title
        for top_comment in post.comments:
            traverse_comments(top_comment, post_title)


        
        

