import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, coin):
        # info-vars
        self.tag = None
        self.name = None

        self.price = None

        self.usd_percentage = None

        self.info = None

        # set-vars
        self.soup = None
        self.r = None

        # main-vars
        self.coin = coin
        self.url = f'https://coinmarketcap.com/uk/currencies/{self.coin}/'
        self.headers = {
            'user-agent': 'YOUR USER-AGENT'}

    def scraper(self):
        self.r = requests.get(self.url, self.headers)
        self.soup = BeautifulSoup(self.r.content, "html.parser")

        self.tag = self.soup.find('small', 'nameSymbol')
        self.name = self.soup.find('span', ['sc-1eb5slv-0', 'sc-1308828-0', 'bwAAhr'])

        self.price = self.soup.find('div', 'priceValue')

        self.usd_percentage = self.soup.find('span', ['sc-15yy2pl-0', 'feeyND'])

    def output(self):
        nums = f'''
        Price : | {self.price.text.replace("UAH", "")} UAH|
        Percentage : | {self.usd_percentage.text} |
        '''

        self.info = (f'''{self.name.text} | {self.tag.text} :
        
        {nums}
        {self.url}''')

        with open('file.txt', 'w') as file:
            file.write(self.info)
            file.close()


if __name__ == '__main__':
    start = Scraper(coin=None)
    start.scraper()
    start.output()
