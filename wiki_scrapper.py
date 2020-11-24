from bs4 import BeautifulSoup
import requests, lxml, re
#import PySimpleGUI as sg

#1 URL to scrap

#Variables
print('Please set the Article you want to scrap. Paste just the url after the /wiki/')
url = input('>')
print('In wich language this article is written?')
lang = input('>')
root = 'https://'+lang+'.wikipedia.org/wiki/'+url

#2 Check in "robots.txt" if it's ok to scrap this URL.

#Check

#Scrap
page = requests.get(root).text
soup = BeautifulSoup(page, 'lxml')


#3 Write the text in a .txt file. OK
with open('note_test.txt', 'w') as f:
    f.write(soup.prettify())
    f.close()
