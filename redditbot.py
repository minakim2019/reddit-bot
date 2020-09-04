#!/usr/bin/python
import praw
import time

reddit = praw.Reddit("config1", user_agent="redditbot1004 user agent")

subreddit = reddit.subreddit("Coronavirus")

#max iterations before termination
max_iterations = 5

# check oauth is working
#print(reddit.user.me())

# for submission in subreddit.hot(limit=5):
#     print("Title: ", submission.title)
#     print("Text: ", submission.selftext)
#     print("Score: ", submission.score)
#     print("---------------------------------\n")

# primary function
#hile(True):
# loop through all submissions
hot_posts = subreddit.hot(limit=10)
for post in hot_posts:
    print(post.title)
    # grab the comments from that submission
    comments = post.comments
    top_score = 0
    top_comment = ''

    # loop through every comment, finding the top score
    # checking praw.helpers.flatten_tree(comments) also checks replies
    for comment in comments:
        comment_text = comment.body.lower()
        comment_score = comment.score
        # find the top scoring comment
        if (comment_score > top_score):
            top_comment = comment_text
            top_score = comment.score


