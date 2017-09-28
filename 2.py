#!/usr/bin/env python
# coding=utf-8
import urllib2
import json
def judge():
   
    print("1.techcrunch-美国科技博客")
    print("2.abc")
    print("3.al-jazeera")
    print("4.ars-technica-美国科技博客")
    print("5.associated-press-美联社")
    print("6.bbc-news")
    print("7.bild-德国图片报-1952")
    print("8.bloomberg")
    print("9.business-insider-美国科技博客")
    print("10.The Economist-经济学人-1843")
    print("11.Reuters-1851")
    print("q-quit")
    url=""
    b=input("please input:")
    a=str(b)
    news=""
    
    if(a=="1"):
        url="https://newsapi.org/v1/articles?source=techcrunch&apiKey=f64790cbb13e402aaa30d41c6f979db1"
        news="techcrunch"
    elif(a=='2'):
        print("*"*25+"abc"+"*"*25)
        url="https://newsapi.org/v1/articles?source=abc-news-au&sortBy=top&apiKey=f64790cbb13e402aaa30d41c6f979db1"
        news="abc"
    elif(a=='3'):
        print("*"*25+"al-jazeera"+"*"*25)
        url="https://newsapi.org/v1/articles?source=al-jazeera-english&sortBy=top&apiKey=f64790cbb13e402aaa30d41c6f979db1"
        news="al-jazeera"
    elif(a=='4'):
        print("*"*25+"ars-technica"+"*"*25)
        url="https://newsapi.org/v1/articles?source=ars-technica&sortBy=top&apiKey=f64790cbb13e402aaa30d41c6f979db1"
        news="ars-technica"
    elif(a=='5'):
        print("*"*25+"associated-press"+"*"*25)
        url="https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey=f64790cbb13e402aaa30d41c6f979db1"
        news="associated-press"
    elif(a=='6'):
        print("*"*25+"bbc-news"+"*"*25)
        url="https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=f64790cbb13e402aaa30d41c6f979db1"
        news="bbc-news"
    elif(a=='7'):
        print("*"*25+"bild"+"*"*25)
        url="https://newsapi.org/v1/articles?source=bild&sortBy=top&apiKey=f64790cbb13e402aaa30d41c6f979db1"
        news="bild"
    elif(a=='8'):
        print("*"*25+"bloomberg"+"*"*25)
        url="https://newsapi.org/v1/articles?source=bloomberg&sortBy=top&apiKey=f64790cbb13e402aaa30d41c6f979db1"
        news="bloomberg"
    elif(a=='9'):
        print("*"*25+"business-insider"+"*"*25)
        url="https://newsapi.org/v1/articles?source=business-insider&sortBy=top&apiKey=f64790cbb13e402aaa30d41c6f979db1"
        news="business-insider"
    elif(a=='10'):
        print("*"*25+"business-insider"+"*"*25)
        url="https://newsapi.org/v1/articles?source=the-economist&sortBy=top&apiKey=f64790cbb13e402aaa30d41c6f979db1"
        news="The Economist"
    elif(a=='11'):
        print("*"*25+"business-insider"+"*"*25)
        url="https://newsapi.org/v1/articles?source=reuters&sortBy=top&apiKey=f64790cbb13e402aaa30d41c6f979db1"
        news="reuters"
    elif(a=='q'):
        print("end")    
    else:
        print("a=1")
    connect(url,news)

    menu=input("menu?1")
   
    if(str(menu)=='1'):
        judge()
    else:
        print("end")
      
def connect(url,news):
    response = urllib2.urlopen(url)
    s=json.load(response)
    ss=s['articles']
    for aa in  ss:
      print("title:"+ aa['title'])
      print("des:"+aa['description'])
      print("url:"+aa['url'])
      print("time:"+aa['publishedAt'])
      print("-"*25+news+"-"*25)
    print("news number:"+str(len(ss)))    
    print("*"*50)
  
if __name__ == "__main__":

    judge()
