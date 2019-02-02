from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find-emotion', methods=['POST'])
def result():
    
    content  = request.form.get('content')
    
    flag, sentiment_meter = get_sentiment(content)   
    
    result = {
        'car_brand' : content,
        'flag': flag,
        'sentiment_meter' : sentiment_meter 
    }
    
    #return content
    return render_template('result.html', result=result)

sid = SentimentIntensityAnalyzer()

def get_sentiment(sentence):
        
    print(sentence)

    ss = sid.polarity_scores(sentence)
    
    #print(type(ss['pos']))

    positive_meter = round((ss['pos'] * 10), 2) 
    negative_meter = round((ss['neg'] * 10), 2)

    '''
    for k in sorted(ss):
        #print(ss)
        print('{0}: {1}, '.format(k, ss[k]), end = '')
    '''

    print('positive : {0}, negative : {1}'.format(positive_meter, negative_meter))

    if(positive_meter > negative_meter):
        return True, positive_meter
    else:
        return False, negative_meter
    
if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host= host, port = port, use_reloader = False)
    
    
'''
Sources:
    http://www.compjour.org/lessons/flask-single-page/multiple-dynamic-routes-in-flask/
    
    https://www.learnpython.org/en/String_Formatting
    
    https://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python
    
    https://github.com/googlemaps/google-maps-services-python
    
    AIzaSyCRhRz_mw_5wIGgF-I6PUy3js6dcY6zQ6Q
    
    Get Current Location:
    https://stackoverflow.com/questions/44218836/python-flask-googlemaps-get-users-current-location-latitude-and-longitude
'''