# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:46:52 2014

@author: eocallaghan
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