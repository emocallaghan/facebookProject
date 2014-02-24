# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:46:52 2014

@author: eocallaghan
"""



from pattern.web import *
f = Facebook(license='CAAEuAis8fUgBAAG8SBjH7bEAimzm6shZBMmOFaginXZCuxdPftGBZBFfHnOYEZAWWBowqHCDzCKNniyeZAm6Feimonnjcgv3hFEG8CLKcbIPHn727Hf9wqPsPV9HNd0V7LHBiN3lUyxWawxmhKbZCtXDjVU6KZBGQ9rLqTgjiHnNvb3CZCkhVzpA36whZB7nRq9EZD')
me = f.profile()
"""
my_friends = f.search(me[0], type=FRIENDS, count=400)
for friend in my_friends:
    friend_news = f.search(friend.id, type=NEWS, count=400)
    for news in friend_news:
        print news.text

"""  
for news in f.search(me[0], type=NEWS, count=100):
    text = str(news.text)
    #print text.contains(me(2))
    name = str(me[1])
    if(not text.__contains__(name)):
        myPost = True
        my_friends = f.search(me[0], type=FRIENDS, count =400)
        for friend in my_friends:
            friend_news = f.search(friend.id, type=NEWS, count =400)
            if (friend_news.id == news.id):
                myPost = False
                break
        if(myPost):
            print repr(text)
    