import bs4 as bs
import os
import requests
import getpass
import time

os.system('cls')

s = requests.session()

# Login
url = 'https://www.gsh-lan.com/login/'
user = input('User: ')
passw = getpass.getpass()
logindata = { 'lg_user': user, 'lg_password': passw }
resp = s.post(url, data=logindata)


# URL to Inbox
url = 'https://www.gsh-lan.com/messages/folder/INBOX/'
# loop infinite
while True:
    os.system('cls')
    # get Messages
    resp = s.get(url)
    #print(resp.content)
    sauce = resp.content
    soup = bs.BeautifulSoup(sauce, 'lxml')

    pns1 = soup.find_all("td", attrs={"class": "msgrow1", "width": "100%"})
    pns2 = soup.find_all("td", attrs={"class": "msgrow2", "width": "100%"})

    pns = pns1 + pns2
    for i, pn in enumerate(pns):
        print(pn.text)

    # refresh every 60 seconds
    time.sleep(60)
