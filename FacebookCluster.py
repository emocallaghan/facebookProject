# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:46:52 2014

@author: eocallaghan
"""
import re, math
from collections import Counter


from pattern.en import *
from pattern.web import *
#Lizzy's Facebook
f_lizzie = Facebook(license='CAAEuAis8fUgBAAG8SBjH7bEAimzm6shZBMmOFaginXZCuxdPftGBZBFfHnOYEZAWWBowqHCDzCKNniyeZAm6Feimonnjcgv3hFEG8CLKcbIPHn727Hf9wqPsPV9HNd0V7LHBiN3lUyxWawxmhKbZCtXDjVU6KZBGQ9rLqTgjiHnNvb3CZCkhVzpA36whZB7nRq9EZD')
#Shrinidhi's Facebook
f_shrin = Facebook(license='CAAEuAis8fUgBAGjbDK3oFYhbFCtymaT4emLFUO2gzgarzB5I9aG4G1ZC7lgvAFnKuT47f0qvvSsKlWuUVF5GOffpbDOORJY68ipZATlyBO43o6ZCXWo3vAIOEi3akZAzfqxp2Heydm3ouLVv9zHHfzbRw9tt7CVOR0Y6ZCHNP1nwqDku7nZADn')

def get_posts(f): #Gets posts and saves in a dictionary
    posts_list = {}
    me = f.profile()
    my_friends = f.search(me[0], type=FRIENDS, count = 10)
    for friend in my_friends:
        friend_name = str(friend.text)
        friend_news = f.search(friend.id, type=NEWS, count =10)
        for news in friend_news:
            post = str(news.text)
            if (not post.__contains__(friend_name)) and (str(news.author).__contains__(friend_name)):
                posts_list[friend_name] = post
    return posts_list

def find_sentiments(friends):
    print friends
    friend_sentiment = {}
    for key in friends:
        print key
        print friends[key]
        analyzed_sentiment = sentiment(friends[key])
        print analyzed_sentiment[0]
        friend_sentiment[key] = analyzed_sentiment[0]
        
    return friend_sentiment

def sort_sentiments(sentiments):
    mostPositive = 0;
    mostPositivePerson = ""
    for key in sentiments:
        if sentiments[key]>mostPositive:
            mostPositive = sentiments[key]
            mostPositivePerson = key
    return mostPositivePerson
    
def sort_sentiments_all(sentiments):
    return sorted(sentiments)
    
#sentimentList = find_sentiments(get_posts(f_lizzie))

#print sort_sentiments(sentimentList)





def word_frequencies(newsFeed):
    word_count = {}
    for i in range(len(newsFeed)):
        current_string = newsFeed[i]
        for j in range(len(current_string)):
            current_word = current_string(j)
            if(word_count.contains_key(current_word)):
                word_count[current_word] = word_count[current_word]+1
            else:
                word_count[current_word] = 1
    return word_count










WORD = re.compile(r'\w+')
#http://stackoverflow.com/questions/15173225/how-to-calculate-cosine-similarity-given-2-sentence-strings-python
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

 
def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

text1 = 'This is a foo bar sentence .'
text2 = 'This sentence is similar to a foo bar sentence .'

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)

cosine = get_cosine(vector1, vector2)


print 'Cosine:', cosine
