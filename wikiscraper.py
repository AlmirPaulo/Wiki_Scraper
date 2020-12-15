import PySimpleGUI as sg
from bs4 import BeautifulSoup
import requests, lxml, re, time

#Windows
def main_win():
    sg.theme('DefaultNoMoreNagging')

    layout = [
        [sg.Text('Url to scrap:')],
        [sg.InputText('https://??.wikipedia.org/wiki/<PASTE THIS PART HERE>', key = 'url')],
        [sg.Text('In wich language this article is written?' ), sg.Combo(['de', 'en', 'es', 'eo', 'el', 'en' , 'fr','vo','pt', 'ru', 'hi', 'it', 'ur', 'ko', 'pl', 'ja', 'gl', 'ro', 'simple', 'la', 'zh',], key = 'lang')],
        [sg.Output(size = ('80', '20'))],
        [sg.Button('Scrap')]
    ]
    return sg.Window('Wiki Scraper', layout, finalize = True)

def alert_win():
    sg.theme('DefaultNoMoreNagging')

    alert_layout = [
        [sg.Text('Sorry, this page is blocked for scraping.')],
        [sg.Button('Ok')]
    ] 
    return sg.Window('Scrap Blocked!', alert_layout, finalize = True)

def loading_win():
    sg.theme('DefaultNoMoreNagging')
    loading_layout = [
            [sg.Text('Just a moment please...')]
        ]


    return sg.Window('Scraping...', loading_layout, finalize = True)

#event loop
main, alert, loading = main_win(), None, None
while True:
    win, ev, values = sg.read_all_windows()
    url = values['url']
    lang = values['lang']
    if win == main and ev == sg.WINDOW_CLOSED:
        break
    if win == main and ev == 'Scrap':
        root = 'https://'+lang+'.wikipedia.org/wiki/'+url
       #2 Check in "robots.txt" if it's ok to scrap this URL.

#variables
        url_ban = re.search(r'Spe.ial:', url)
        url_ban2 = re.search(r'Spe.ial%3A', url)
#Check
        if url_ban != None:
            alert = alert_win()
            main.hide()
        elif url_ban2 != None:
            alert = alert_win()
            main.hide()
        else:
            loading = loading_win()
            time.sleep(10)
            loading.hide()
#Scrap
            page = requests.get(root).text
            soup = BeautifulSoup(page, 'lxml')
            tag = soup.find_all('p')
            for i in tag:
                print(i.text)
    if win == alert and ev == 'Ok':
        alert.hide()
        main.un_hide()
