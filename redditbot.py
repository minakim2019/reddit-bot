#!/usr/bin/python3
import praw
import time
import pandas as pd
import textwrap

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

topics_dict = { "title":[], \
                "score":[], \
                "id":[],\
                "created": []}

hot_posts = subreddit.hot(limit=10)
for post in hot_posts:
    print(color.BOLD + post.title + color.END)
    #specifies to not load more top comments
    post.comments.replace_more(limit=0)
    #iterates through top comments, printing them
    count = 0
    print(color.UNDERLINE + "Top Comments:" + color.END)
    for top_level_comment in post.comments:
        comment_text = textwrap.dedent(top_level_comment.body).strip()
        print(textwrap.fill(comment_text, width = 60))
        print('\n')
        count+=1
        if count == 2:
            break

    #posts = []
    #posts.append(
        #[post.title, post.score, post.num_comments, post.selftext, post.created])
    #posts = pd.DataFrame(posts,
                            #columns=['title', 'score', 'num_comments', 'body', 'created'])
    #print(posts)
    #collect data
    #topics_dict["title"].append(post.title)
    #topics_dict["score"].append(str(post.score))
    #topics_dict["id"].append(post.id)
    #topics_dict["created"].append(str(post.created))
    #topics_dict["top_comment"].append(post.)


#date to readable timestamp format
#def get_date(created):
    #return dt.datetime.fromtimestamp(created)
#_timestamp = topics_data["created"].apply(get_date)
#topics_data = topics_data.assign(timestamp = _timestamp)


# store everything into a file
file = open('file.txt', 'w')#.write(output)

# header to the file
file.write('Top 10 Posts Today from r/Coronavirus' + '\n')
file.write('-------------------------------------' + '\n\n')