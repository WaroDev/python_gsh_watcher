#!/usr/local/bin/python3

from getpass import getpass
from clize import run
from bs4 import BeautifulSoup
import requests

URL = "https://www.gsh-lan.com"
URL_LOGIN = "https://www.gsh-lan.com/user/?do=login"


def main():
    """ GSH Forum and Match watcher & notifier
    """
    # get login data
    username = input("User: ")
    password = getpass()

    # login into the site
    x = requests.get(URL_LOGIN)
    soup = BeautifulSoup(x.text, 'html.parser')

    print(soup.prettify())


if __name__ == "__main__":
    run(main)
