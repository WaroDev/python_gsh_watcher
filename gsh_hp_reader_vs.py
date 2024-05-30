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

contestId = input("Contest-Id: ")

# URL to Inbox
url = 'https://www.gsh-lan.com/turnier/contest/' + contestId + '/'

#get title
resp = s.get(url)
sauce = resp.content
soup = bs.BeautifulSoup(sauce, 'lxml')
title = soup.find_all("h1")[0]
#set title
os.system('title ' + title.text)

# loop infinite
while True:
    os.system('cls')
    # get Messages
    resp = s.get(url)
    #print(resp.content)
    sauce = resp.content
    soup = bs.BeautifulSoup(sauce, 'lxml')

    posts = soup.find_all("td", attrs={"class": "forumpostingcontent"})
    for i, post in enumerate(posts):
        print(post.text.strip())
        print("=================")
        print("")

    # refresh every 60 seconds
    time.sleep(60)
