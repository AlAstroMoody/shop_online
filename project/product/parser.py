import csv
from multiprocessing import Pool

import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_all_links(html):
    catalog_url = 'https://www.bliz.ru/catalog'
    soup = BeautifulSoup(html, "html.parser")
    pages = soup.find('div', class_='catalog-right').find_all('a', class_='catalog-name')
    links = []
    for page in pages:
        link = page.get('href')
        links.append(catalog_url + link)
    return links


def get_all_information(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    uid, image_url, category, name = '', '', '', ''
    try:
        coincidences = soup.find('div', class_='itemPage-description').find_all('div', class_='desc-row')
        for coincidence in coincidences:
            string = coincidence.text.strip()
            if string.startswith('Код запчасти:'):
                uid = string[14:]
    except AttributeError:
        uid = 'тут ошибка'
        print(url, uid)

    # name = soup.find('div', class_='itemPage-info').find('h1').text.strip()
    names = soup.find_all('li', itemprop='itemListElement')
    for name in reversed(names):
        name = name.text.strip()
        break

    brand = soup.find('div', class_='desc-row').find('a').text.strip()
    try:
        price = soup.find('div', class_='amount').find('span', class_='price_val').text.strip()
    except AttributeError:
        price = 'уточните цену'

    description = soup.find('div', class_='content-description').text.strip()
    check = True
    image = soup.find('a', class_='mainImg').get('href')
    url = 'https://www.bliz.ru/data/image/catalog/'
    for i in range(len(image)):
        if image[i] == '_':
            image_url = url + image[i + 1:-3] + 'JPEG'
            if len(image_url) > 90:  # иногда в этом месте сбои при многопоточной обработке, проверка
                check = False  # пропускаем такие ссылки
                break

    categories = soup.find_all('a', itemprop="item")
    for i in range(len(categories)):
        if i == 2:
            category = categories[i].text.strip()
            break
    print(uid, '- OK')
    with open('../media/detail.csv', 'a', encoding='utf-8') as output:
        writer = csv.writer(output)
        result_row = (name, brand, uid, price, description, image_url, category)
        if check:
            writer.writerow(result_row)


def main():
    url = 'https://www.bliz.ru/catalog/page/2?ls=40'
    html = get_html(url)
    links = get_all_links(html)
    with open('../media/detail.csv', 'a', encoding='utf-8') as output:
        writer = csv.writer(output)
        result_row = 'name', 'brand', 'uid', 'price', 'description', 'image_url', 'category'
        writer.writerow(result_row)
    with Pool(4) as p:
        p.map(get_all_information, links)


if __name__ == '__main__':
    main()
