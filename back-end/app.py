from flask import Flask, jsonify
#from flask_cors import CORS
import praw
import json

# initialize with appropriate values 
client_id = "6SVrWF9tph3rr3-r98E1VA" 
client_secret = "Jx_HLO3mLeVTTHMkAjHMSmbZqG2WcA" 
username = "SourceScanCSC468" 
password = "Group8jamds" 
user_agent = "SourceScan"

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, username=username, password=password, user_agent=user_agent)
subred = 'Bitcoin'
subreddit_names = ['news', 'worldnews', 'politics', 'technews']
articles = []
def get_top_articles(subred):
    
    for subreddit_name in subreddit_names:
        subreddit = reddit.subreddit(subreddit_name)
        for submission in subreddit.search(subred, sort='top', time_filter='week', limit=3):
            article = {
                'subreddit': subreddit_name,
                'title': submission.title,
                'score': submission.score,
                'url': submission.url
            }
            articles.append(article)
    return articles






app = Flask(__name__)
#CORS(app)

@app.route("/point")
def data():  

    articles = get_top_articles(subred)
    if len(articles) < 1:
        return jsonify({'error': 'No top articles found'})
    my_dict = {
        "Subreddit": articles[0]['subreddit'],
        "Title": articles[0]['title'],
        "Score": articles[0]['score'],
        "URL": articles[0]['url']
    }
    return jsonify(my_dict)
    #return jsonify(type(my_dict))


if __name__== "__main__":
    app.run(debug = True)

