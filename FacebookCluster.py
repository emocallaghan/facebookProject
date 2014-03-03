# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:46:52 2014

@author: eocallaghan
"""

from pattern.en import *
from pattern.web import *
#Lizzy's Facebook
f_lizzie = Facebook(license='CAAEuAis8fUgBAAG8SBjH7bEAimzm6shZBMmOFaginXZCuxdPftGBZBFfHnOYEZAWWBowqHCDzCKNniyeZAm6Feimonnjcgv3hFEG8CLKcbIPHn727Hf9wqPsPV9HNd0V7LHBiN3lUyxWawxmhKbZCtXDjVU6KZBGQ9rLqTgjiHnNvb3CZCkhVzpA36whZB7nRq9EZD')
#Shrinidhi's Facebook
f_shrin = Facebook(license='CAAEuAis8fUgBAGjbDK3oFYhbFCtymaT4emLFUO2gzgarzB5I9aG4G1ZC7lgvAFnKuT47f0qvvSsKlWuUVF5GOffpbDOORJY68ipZATlyBO43o6ZCXWo3vAIOEi3akZAzfqxp2Heydm3ouLVv9zHHfzbRw9tt7CVOR0Y6ZCHNP1nwqDku7nZADn')

def get_posts(f): #Gets posts and saves in a dictionary
    posts_list = {}
    me = f.profile()
    my_friends = f.search(me[0], type=FRIENDS, count = 200)
    for friend in my_friends:
        friend_name = str(friend.text)
        friend_news = f.search(friend.id, type=NEWS, count =10)
        for news in friend_news:
            post = str(news.text)
            if (not post.__contains__(friend_name)) and (str(news.author).__contains__(friend_name)):
                posts_list[friend_name] = post
    return posts_list

def find_sentiments(friends):
    friend_sentiment = {}
    for key in friends:
        analyzed_sentiment = sentiment(friends[key])
        friend_sentiment[key] = analyzed_sentiment[0]
        
    return friend_sentiment

def find_subjectivity(friends):
    friend_subjective = {}
    for key in friends:
        analyzed_subjective = sentiment(friends[key])
        friend_subjective[key] = analyzed_subjective[1]
        
    return friend_subjective
    
def most_Positive_Person(sentiments):
    mostPositive = -1;
    mostPositivePerson = ""
    for key in sentiments:
        if sentiments[key]>mostPositive:
            mostPositive = sentiments[key]
            mostPositivePerson = key
    return mostPositivePerson
    
def most_negative_Person(sentiments):
    mostNegative = 1;
    mostNegativePerson = ""
    for key in sentiments:
        if sentiments[key]<mostNegative:
            mostNegative = sentiments[key]
            mostNegativePerson = key
    return mostNegativePerson
    
def sort_sentiments_postive(sentiments):
    positivePeople = []
    for people in sorted(sentiments, key=sentiments.get, reverse=True):
        positivePeople.append(people)
    return positivePeople
        
def sort_sentiments_negative(sentiments):
    negativePeople = []
    for people in sorted(sentiments, key=sentiments.get):
        negativePeople.append(people)
    return negativePeople
    
def most_subjective(subjectivity):
    mostSubjective = 0;
    mostSubjectivePerson = ""
    for key in subjectivity:
        if subjectivity[key]>mostSubjective:
            mostSubjective = subjectivity[key]
            mostSubjectivePerson = key
    return mostSubjectivePerson
    
def most_objective(subjectivity):
    mostObjective = 1;
    mostObjectivePerson = ""
    for key in subjectivity:
        if subjectivity[key]<mostObjective:
            mostObjective = subjectivity[key]
            mostObjectivePerson = key
    return mostObjectivePerson
    
def sort_subjectivity(subjectivy):
    subjectivePeople = []
    for people in sorted(subjectivy, key=subjectivy.get, reverse=True):
        subjectivePeople.append(people)
    return subjectivePeople
        
def sort_objectivity(subjectivy):
    objectivePeople = []
    for people in sorted(subjectivy, key=subjectivy.get):
        objectivePeople.append(people)
    return objectivePeople
    
posts = get_posts(f_lizzie)
    
sentimentList = find_sentiments(posts)
subjectiveList = find_subjectivity(posts)

print sort_sentiments_postive(sentimentList)
print sort_sentiments_negative(sentimentList)

print sort_subjectivity(subjectiveList)
print sort_objectivity(subjectiveList)

print most_subjective(subjectiveList)
print most_objective(subjectiveList)