from bs4 import BeautifulSoup
import requests, lxml, re, time


#1 URL to scrap

#Variables
print('Please set the Article you want to scrap. Paste just the url after the /wiki/')
url = input('>')
print('In wich language this article is written?')
lang = input('>')
root = 'https://'+lang+'.wikipedia.org/wiki/'+url

#root = 'http://localhost:8000/'+url

#2 Check in "robots.txt" if it's ok to scrap this URL.

#variables
url_ban = re.search(r'Spe.ial:', url)
url_ban2 = re.search(r'Spe.ial%3A', url)
#Check
if url_ban != None:
    print("I'm sorry, this page is blocked for scrapings")
elif url_ban2 != None:
    print("I'm sorry, this page is blocked for scrapings")
else:
#Scrap
    print('Just a moment please...')
    time.sleep(10)
    page = requests.get(root).text
    soup = BeautifulSoup(page, 'lxml')
#3 Write the text in a .txt file. 
    with open('wikiscrap.txt', 'w') as f:
        f.write()
        f.close()
    print('Done! Go check your files.')
