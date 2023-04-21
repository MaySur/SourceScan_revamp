import praw

client_id = "bG7tZ2k68opbl9agjUeqgg" 
client_secret = "nkHxd3nTPezesMzUB2AbG56e0FT2rg" 
user_agent = "maysur_sourcescan"
red = praw.Reddit(client_id = client_id, client_secret = client_secret, user_agent = user_agent)
user_inp = "Microsoft"

sub_names = ['news', 'worldnews', 'politics', 'technews']
articles = []

def Article() :
    for i in sub_names:
        count = 1
        r_sub = red.subreddit(i)
        for j in r_sub.search(user_inp, sort='top', time_filter='week', limit = 3):
            article = {
                'id' : count,
                'subreddit': 'r/'+i,
                'title': j.title,
                'score': j.score,
                'url': j.url
            }
            articles.append(article)
            count+=1
    print(articles)
    return articles

Article() 

