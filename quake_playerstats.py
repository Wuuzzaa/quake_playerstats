import urllib.request
from bs4 import BeautifulSoup as Bs
import time

URL = "http://steamcharts.com/app/611500"
FILE_NAME = "qc_player_stats.csv"


def get_onlineplayers():
    """
    Scrap the URL to find the current online Players.
    :return: Amount of online players
    """
    source = urllib.request.urlopen(URL)
    soup = Bs(source, "html.parser")
    player_box = soup.find("span", attrs={"class": "num"})
    player_count = player_box.text.strip()
    return player_count


def write_to_csv(file_name, date, players):
    text = date + "," + players
    print(text)
    with open(file_name, mode="a") as file:
        file.write(text)



players = get_onlineplayers()
date = time.strftime("%d.%m.%Y %H:%M:%S")

write_to_csv(FILE_NAME, date, players)