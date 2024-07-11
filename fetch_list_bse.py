from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import time

# make get request for html page
# url = "https://www.screener.in/screens/41897/all-bse-companies/?page=1"
# req = requests.get(url)
# print(req.text)


# # create a soup
# soup = BeautifulSoup(req.text, 'html.parser')
# # print(soup)

# table = soup.find("table", {"class": "data-table"})
# tr = table.findAll("tr")[1:]
arr = []
for page in tqdm(range(1, 188)):
    url = f"https://www.screener.in/screens/41897/all-bse-companies/?page={page}"
    req = requests.get(url)

    time.sleep(1)

    soup = BeautifulSoup(req.text, 'html.parser')
    table = soup.find("table", {"class": "data-table"})
    tr = table.findAll("tr")[1:]
    # print(page)

    for _tr in tr:
        td = _tr.findAll("a", {"target": "_blank"})
        if td:
            arr.append(td[0].text)
    
print(len(arr))
