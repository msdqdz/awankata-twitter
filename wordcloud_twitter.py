# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 03:56:41 2021

@author: MSD
"""

#import required packages
import tweepy
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

cari = str(input("Mau cari apa? "))
print("Silakan tunggu...")

#Create variables for API twitter information
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

#Request authentication 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Define tweetSearch
def tweetSearch(query, limit = 10, language = "id"):
    text = ""
    for tweet in tweepy.Cursor(api.search, q=query, lang=language).items(limit):
        text += tweet.text.lower()
    return text

#Define wordcloud plot
def plot_cloud(wordcloud):
    plt.figure(figsize=(40,30))
    plt.imshow(wordcloud, interpolation = "bilinear")
    plt.axis("off")
    #Save plot image to file with names
    plt.savefig(cari + '.png', bbox_inches='tight')

search = tweetSearch(cari)
stop_words = ["https","amp","rt","gw","lo","gue",'lu','gua',"loe","jika","apa","jadi","seperti","ke","t","di","http","ini","itu","co",'com',"pada","ia","akan","tidak","iya","ya","tp","yg","ku","bahwa","dan","yang","di","dengan","juga","sebagaimana","oleh","menjadi","namun","tapi","dari"] + list(STOPWORDS)
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='Pastel1', collocations=False, stopwords = stop_words).generate(search)

#Tampilkan wordcloud
x = plot_cloud(wordcloud)
print(x)

if x != False:
    print('silakan cek file')
    