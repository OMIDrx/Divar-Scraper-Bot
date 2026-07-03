import requests
from bs4 import BeautifulSoup


def get_ads():

    url = 'https://divar.ir/s/ahvaz'

    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
    
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    ads = soup.find_all('article')

    result = []
    
    for ad in ads:

        title = ad.find('h2')
        price = ad.find('div',class_='kt-post-card__description')
        link = ad.find('a')

        if title:

            if price:
                price_text = price.get_text(strip=True)
            else:
                price_text = 'نامشخص'

            if link:
                link_text = 'https://divar.ir' + link.get('href')
            else:
                link_text = ''

            result.append({
                'title': title.get_text(strip=True),
                'price': price_text,
                'link': link_text
            })

    return result


if __name__ == '__main__':

    data = get_ads()

    print('Number Of Ads :', len(data))
    print('=' * 50)

    for item in data:

        print(item['title'])
        print(item['price'])
        print(item['link'])
        print('-' * 50)
        
