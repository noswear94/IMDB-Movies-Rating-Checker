import os
from bs4 import BeautifulSoup
import requests
import urllib.request
import re


def links(url):
    try:
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")

        link = str(soup.find("td",{"class":"result_text"}));
        #print(link)

        start = 'href="'
        end = '"'
        result = re.search('%s(.*)%s' % (start, end), link).group(1)
        #print(result)

        prefix = "https://www.imdb.com"
        rating_link = prefix + result
        ratings(rating_link)
    except:
        print("\n")
        pass

def ratings(rating_link):
    #print(rating_link)
    source_code_rate = requests.get(rating_link)

    plain_text_rate = source_code_rate.text
    soup_rate = BeautifulSoup(plain_text_rate,"html.parser")
    rate = soup_rate.find("span",{"itemprop":"ratingValue"});
    name = soup_rate.find("h1",{"itemprop":"name"});
    genre_list=[]
    for x in soup_rate.find_all("span",{"itemprop":"genre"}):
         genre = x.text
         genre_list.append(genre)

    print(""," "*(50-len(name.text)),name.text," "*(45-len(name.text)),"",rate.text," "*(18-len(rate.text)),genre_list)


def main():
    arr = os.listdir('D:/movie/Docu')
    Base_url = "http://www.imdb.com/find?s=tt&q="
    for x in arr:
        x = x.split(']')[0]
        x = x.split(')')[0]
        x = x.replace('.avi','')
        x = x.replace('.mp4','')
        x = x.replace('.mkv','')
        x = x.replace('.com','')
        x = x.replace('.',' ')
        x = x.replace('_',' ')
        x = x.split('720')[0]
        x = x.split('1080')[0]
        x = x.split('HD')[0]
        x = x.split('480')[0]
        x = x.split('DVD')[0]
        x = x.split('WorldFree')[0]
        x = x.split('Blu')[0]
        x = x.split('BDRip')[0]
        x = x.split('720')[0]





        print(x,end="")
        url = "http://www.imdb.com/find?s=tt&q=%s"%(x)
        links(url)


print("Searching for \t\t\t\t\t\t\t\t\t Searched \t\t\t\t\t\t\t\t\t\tRating\t\t\t\t\t\t\t\t Genre")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
main()

