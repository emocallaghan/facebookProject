# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:46:52 2014

@author: sthirumalai and eocallaghan
"""


#importing pattern to be used to fetch facebook data
from pattern.web import *
#Lizzy's Facebook liscence
f_lizzie = Facebook(license='CAAEuAis8fUgBAAG8SBjH7bEAimzm6shZBMmOFaginXZCuxdPftGBZBFfHnOYEZAWWBowqHCDzCKNniyeZAm6Feimonnjcgv3hFEG8CLKcbIPHn727Hf9wqPsPV9HNd0V7LHBiN3lUyxWawxmhKbZCtXDjVU6KZBGQ9rLqTgjiHnNvb3CZCkhVzpA36whZB7nRq9EZD')
#Shrinidhi's Facebook liscence
f_shrin = Facebook(license='CAAEuAis8fUgBAGjbDK3oFYhbFCtymaT4emLFUO2gzgarzB5I9aG4G1ZC7lgvAFnKuT47f0qvvSsKlWuUVF5GOffpbDOORJY68ipZATlyBO43o6ZCXWo3vAIOEi3akZAzfqxp2Heydm3ouLVv9zHHfzbRw9tt7CVOR0Y6ZCHNP1nwqDku7nZADn')

def get_posts_string(news_list, name, num):
    """
    Takes input of a list of all posts related to a friend, only filters out statuses,
    and outputs them in one string with all statuses seperated by spaces.
    """
    friend_statuses = '' #initializes string of statuses
    #iterates through all posts
    for news in news_list:
        post = str(news.text) #gets text of each status
        #filters out only posts made by friend
        if (not post.__contains__(name)) and (str(news.author).__contains__(name)):
            #if post is on someone elses wall, filters out only the text posted on wall
            if post.__contains__('"'):
                start = post.index('"')
                end = (post[start:]).index('"')
                post = post[start:end]
            #creates concatinated string of all statuses
            friend_statuses = friend_statuses + ' ' + post
    print num #debugging helper
    return friend_statuses
    
def get_posts(f): 
    """ 
    1. Goes through all friends of user of inputted facebook liscence
    2. Gets all statuses of each friend and concatinates all statuses into one string
    3. Creates a dictionary with the keys as the facebook friend and the value as the string of statuses
    """
    posts_list = {} #initializes dictionary
    me = f.profile() #gets profile from given liscence
    my_friends = f.search(me[0], type=FRIENDS, count=100)
    tick = 0 #debugging helper
    #iterates through all friends of user
    for friend in my_friends:
        tick = tick + 1 #debugging helper: prints out iteration of friend
        friend_name = str(friend.text)
        #gets all posts related to friend, passes if none are found
        try:
            friend_news = f.search(friend.id, type=NEWS, count =20, timeout = 5)
        except URLTimeout:
            pass
        #creates dictionary of friends with statuses
        posts_list[friend_name] = get_posts_string(friend_news, friend_name, tick)
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

    
"""    
#print str(me[0])  
for news in f.search(me[0], type=NEWS, count=100):
    #text = str(news.text)
    #print text
    #print str(post.id)
    #print type(me)    
    #print type(post)
    author = str(news.author)
    name = str(me[1])
    if(author.__contains__(name)):
        if()
        print news.text
        #print post.story_tags
        
    
    """

