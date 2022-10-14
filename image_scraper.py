import requests
from bs4 import BeautifulSoup
import os

#url = 'https://www.jumia.com.ng/phones-tablets/'


def imageDownloader(url, folder):
    os.mkdir(os.path.join(os.getcwd(), folder))
    os.chdir(os.path.join(os.getcwd(), folder))

    scrap_img = requests.get(url)
    soup = BeautifulSoup(scrap_img.text, 'lxml')
    images = soup.find_all('img')

    i = 1
    try:
        for image in images:
            # name = image.find('alt')['alt']
            link = image['data-src']
            name = str(i)
            i += 1
            with open(name + '.jpeg', 'wb') as f:
                im = requests.get(link)
                f.write(im.content)
                print(f'Downloding photo {name}')
    except Exception as e:
        print('Broken link')


imageDownloader('https://www.jumia.com.ng/phones-tablets/', 'ScrapedImages')
