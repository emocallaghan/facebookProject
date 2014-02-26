# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:46:52 2014

@author: eocallaghan
"""



from pattern.web import *
#Lizzy's Facebook
f_lizzie = Facebook(license='CAAEuAis8fUgBAAG8SBjH7bEAimzm6shZBMmOFaginXZCuxdPftGBZBFfHnOYEZAWWBowqHCDzCKNniyeZAm6Feimonnjcgv3hFEG8CLKcbIPHn727Hf9wqPsPV9HNd0V7LHBiN3lUyxWawxmhKbZCtXDjVU6KZBGQ9rLqTgjiHnNvb3CZCkhVzpA36whZB7nRq9EZD')
#Shrinidhi's Facebook
f_shrin = Facebook(license='CAAEuAis8fUgBAGjbDK3oFYhbFCtymaT4emLFUO2gzgarzB5I9aG4G1ZC7lgvAFnKuT47f0qvvSsKlWuUVF5GOffpbDOORJY68ipZATlyBO43o6ZCXWo3vAIOEi3akZAzfqxp2Heydm3ouLVv9zHHfzbRw9tt7CVOR0Y6ZCHNP1nwqDku7nZADn')

def get_posts(f): #Gets posts and saves in a dictionary
    posts_list = {}
    me = f.profile()
    my_friends = f.search(me[0], type=FRIENDS, count=400)
    for friend in my_friends:
        friend_name = str(friend.text)
        friend_news = f.search(friend.id, type=NEWS, count =100)
        for news in friend_news:
            post = str(news.text)
            if (not post.__contains__(friend_name)) and (str(news.author).__contains__(friend_name)):
                posts_list[friend_name] = post
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