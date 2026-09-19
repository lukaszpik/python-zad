from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "https://static.nbp.pl/dane/stopy/stopy_procentowe.xml"
    xml = requests.get(url, headers={"User-Agent": "Unknown"})
    BS = BeautifulSoup(xml.text, 'lxml')
    for z in BS.find("tabela").find_all("pozycja"):
        print(z["nazwa"], z["oprocentowanie"])