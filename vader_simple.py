#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on Aug 26, 2017

Ref:
https://pythonspot.com/category/nltk/

@author: raja

http://t-redactyl.io/blog/2017/04/using-vader-to-handle-sentiment-analysis-with-social-media-text.html

https://stackoverflow.com/questions/40481348/is-it-possible-to-edit-nltks-vader-sentiment-lexicon
'''


from nltk.sentiment.vader import SentimentIntensityAnalyzer

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
    
    print()    


def main():
    
    content = 'I am so happy today'
       
    get_sentiment(content)
    print('---')            
        
    
if __name__ == '__main__':
    main()