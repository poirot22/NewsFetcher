import requests
from bs4 import BeautifulSoup as bs

class Fetcher:
    websites = {
        "guardian": "https://www.theguardian.com/international",
        "aljazeera": "https://www.aljazeera.com",
        "print": "https://theprint.in/",
        "toi": "https://timesofindia.indiatimes.com"
    }

    def getGuardianHeadlines(self):

        response = requests.get(self.websites["guardian"])

        soup = bs(response.content, 'html.parser')
        news = soup.find_all("a", class_="u-faux-block-link__overlay js-headline-text")

        headlines = {

        }

        for i in news[:5]:
            headlines[i.text] = i['href']

        return headlines

    def getAlJazeeraHeadlines(self):

        response = requests.get(self.websites["aljazeera"])
        soup = bs(response.content, 'html.parser')

        news = soup.find_all("a", class_="fte-article__title-link u-clickable-card__link")
        headlines = {

        }

        # print(r)
        for i in news[:5]:
            t = str(i.findChild("span"))
            t = t[6::]
            t = t[(-1) * len(t):-7:]

            headlines[t] = "aljazeera.com" + i['href']

        return headlines

    def getPrintHeadlines(self):

        response = requests.get(self.websites["print"])
        soup = bs(response.content, 'html.parser')

        news = soup.find_all("h3", class_="entry-title td-module-title")
        c = []
        for i in news:
            c.append(i.findChild("a", recursive=False))

        headlines = {

        }

        for i in c[:5]:
            headlines[i["title"]] = i["href"]

        return headlines

    def getTOIHeadlines(self):
        response = requests.get(self.websites["toi"])
        soup = bs(response.content, 'html.parser')

        news = soup.find("div", class_="_2r4Y_ _3abpr grid_wrapper")

        c = news.findChildren("figcaption")
        # print(c)

        k = []

        for i in news:
            try:
                k.append((i.findChild("a")["href"]))
            except:
                pass

        headlines = {

        }

        for i in range(6):
            headlines[c[i].text] = k[i]

        return headlines



