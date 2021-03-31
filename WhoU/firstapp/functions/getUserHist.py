import requests
from bs4 import BeautifulSoup

def f(vk_id):
    DOLLAR_RUB = "https://vk.com/" + vk_id
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    full_page = requests.get(DOLLAR_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    ssilka_na_avy = str(soup.findAll("img", {"class": "page_avatar_img"}))
    ssilka_na_avy = ssilka_na_avy.split(" src=")[1]
    ssilka_na_avy = ssilka_na_avy.split(" alt")[0]
    ssilka_na_avy = ssilka_na_avy[1: len(ssilka_na_avy) - 1]
    ssilka_na_avy = ssilka_na_avy.replace("amp;", "")
    return ssilka_na_avy if ssilka_na_avy != '/images/deactivated_hid_200.gif"/>' else None
