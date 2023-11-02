import requests
from bs4 import BeautifulSoup





target_url="your url"


link_list=[]



def all_links_finder(linkx):
    textt = requests.get(linkx)
    soup = BeautifulSoup(textt.content, "html.parser")
    for link in soup.find_all('a', href=True):
        k=link.get("href")

        if  "http" in k and k not in link_list:
            link_list.append(k)
            print(k)
            all_links_finder(k)


all_links_finder(target_url)
print(len(link_list))








