#!/usr/bin/python3
import praw
import time
import pandas as pd
import textwrap
import datetime as dt

#color configurations
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#configuration/oauth
reddit = praw.Reddit("config1", user_agent="redditbot1004 user agent")
subreddit = reddit.subreddit("Coronavirus")


# store everything into a file
#file = open('file.txt', 'w')#.write(output)

# header to the file
#file.write('Top 10 Posts Today from r/Coronavirus' + '\n')
#file.write('-------------------------------------' + '\n\n')

print(color.BOLD + color.RED + 'Top 10 Posts Today from r/Coronavirus' + color.END)
hot_posts = subreddit.hot(limit=10)
for post in hot_posts:
    #print post title
    print(color.BOLD + post.title + color.END)
    #print timestamp in readable format
    print(dt.datetime.fromtimestamp(post.created))
    #specifies to not load more top comments
    post.comments.replace_more(limit=0)
    #iterates through top comments, printing them
    count = 0
    print(color.UNDERLINE + "Top Comments:" + color.END)

    for top_level_comment in post.comments:
        print("[Comment Score: " + str(top_level_comment.score) + "]")
        comment_text = '"' + textwrap.dedent(top_level_comment.body).strip() + '"'
        print(textwrap.fill(comment_text, width = 60))
        print('\n')
        count+=1
        #limit to 2 top comments per post
        if count == 2:
            break


