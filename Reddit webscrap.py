import praw
import pandas as pd
import datetime as dt
from psaw import PushshiftAPI



reddit = praw.Reddit(client_id = 'VQ9-xzXLfnf5fA',client_secret = 'oIbS9vZ7iYORM6KFWliekzgYcy0IWA'
,user_agent = 'webScraping')

#Printing in terminal window
posts =[]

#top_posts = reddit.subreddit('Bitcoin').hot(limit=10)
#for post in top_posts:
    #print(post.title)
#Using Pandas to present as table
    #posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])

#posts = pd.DataFrame(posts,columns=['title', 'score', 'id','subreddit','url','num_comments', 'body', 'created'])
#post.to_excel('Top infidelity posts', index = False, header = False)
#print(posts)

#Reddit API useful, but lacks advanced search, t
# thus the use  of PUSHSHIFT.IO API

api = PushshiftAPI()

start_time = int(dt.datetime(2021,6,26).timestamp())
end_time = int(dt.datetime(2021,6,29).timestamp())

print(list(api.search_submissions(after = start_time, before = end_time, subreddit = 'Cryptocurrency')))
filter = ['url','author','title','subreddit']
