# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:46:52 2014

@author: eocallaghan
"""



from pattern.web import *
f = Facebook(license='CAAEuAis8fUgBAAG8SBjH7bEAimzm6shZBMmOFaginXZCuxdPftGBZBFfHnOYEZAWWBowqHCDzCKNniyeZAm6Feimonnjcgv3hFEG8CLKcbIPHn727Hf9wqPsPV9HNd0V7LHBiN3lUyxWawxmhKbZCtXDjVU6KZBGQ9rLqTgjiHnNvb3CZCkhVzpA36whZB7nRq9EZD')
me = f.profile()

my_friends = f.search(me[0], type=FRIENDS, count=400)
for friend in my_friends:
    friend_name = str(friend.text)
    for news in f.search(friend.id, type=NEWS, count =100):
        friend_text = str(news.text)
        if (not friend_text.__contains__(friend_name)):
            news_author = str(news.author)
            if(news_author.__contains__(friend_name)):
                print news.text

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