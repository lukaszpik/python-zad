from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "https://archiwum.mat.umk.pl/web/wmii/wydzial/nauczyciele-akademiccy"
    html = requests.get(url, headers={"User-Agent": "Unknown"})
    result = []
    BS = BeautifulSoup(html.text, 'html.parser')
    L = BS.find("table").find_all("tr")[1:]
    m = len(L)
    n = 1
    for row in L:
        print(str((100*n)//m) + "%", end="")
        n += 1
        col = row.find("td")
        html_empl = requests.get(col.find("a")["href"], headers={"User-Agent": "Unknown"})
        BS_empl = BeautifulSoup(html_empl.text, 'html.parser')
        for row_empl in BS_empl.find("table").find_all("tr"):
            col_empl = row_empl.find_all("td")
            if(col_empl[0].text == "Jednostka organizacyjna Wydziału"):
                result.append([col.text.strip(), col_empl[1].text])

        print("\r", end="")

    print(result)