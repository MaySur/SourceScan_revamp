import praw

client_id = "bG7tZ2k68opbl9agjUeqgg" 
client_secret = "nkHxd3nTPezesMzUB2AbG56e0FT2rg" 
user_agent = "maysur_sourcescan"

red = praw.Reddit(client_id = client_id, client_secret = client_secret, user_agent = user_agent)
user_inp = input('Give Keyword:')

sub_names = ['news', 'worldnews', 'politics', 'technews']
articles = []

for i in sub_names:
    r_sub = red.subreddit(i)
    for j in r_sub.search(user_inp, sort='top', time_filter='week', limit = 3):
        article = {
            'subreddit': 'r/'+i,
            'title': j.title,
            'score': j.score,
            'url': j.url
        }
        articles.append(article)


def write_list_to_file(file_path, lst):
    with open(file_path, 'w') as file:
        for item in lst:
            file.write("%s\n" % item)


write_list_to_file('first.txt', articles)


'''
from flask import Flask, jsonify, request
import praw
import json

client_id = "bG7tZ2k68opbl9agjUeqgg" 
client_secret = "nkHxd3nTPezesMzUB2AbG56e0FT2rg" 
user_agent = "maysur_sourcescan"


red = praw.Reddit(client_id = client_id, client_secret = client_secret, user_agent = user_agent)
user_inp =  'trump'  #input('Give Keyword:')
sub_names = ['news', 'worldnews', 'politics', 'technews']
articles = []

for i in sub_names:
    r_sub = red.subreddit(i)
    for j in r_sub.search(user_inp, sort='top', time_filter='week', limit = 3):
        article = {
            'subreddit': 'r/'+i,
            'title': j.title,
            'score': j.score,
            'url': j.url
        }
        articles.append(article) 

app = Flask(__name__)
#CORS(app)

@app.route("/point", methods = ['POST'])
def handle_state_var(): 
    data = request.json
    state_variable = data['stateVariable']
    return state_variable


def data():  

    for i in sub_names:
        r_sub = red.subreddit(i)
        for j in r_sub.search(user_inp, sort='top', time_filter='week', limit = 3):
            article = {
                'subreddit': 'r/'+i,
                'title': j.title,
                'score': j.score,
                'url': j.url
            }
            articles.append(article)

            
    return jsonify(articles)

    #return jsonify(type(my_dict))


if __name__== "__main__":
    app.run(debug = True)



'''