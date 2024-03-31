import bs4
import requests
from fake_headers import Headers
from pprint import pprint
def get_headers():
    return Headers(os='win', browser='chrome').generate()

site = 'https://habr.com/ru/articles/'
site1 = 'https://habr.com'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get(url=site,headers=get_headers())

main_html = response.text

soup = bs4.BeautifulSoup(main_html,features='lxml')
pars_data = []
vse_stat = soup.find(name='div', class_='tm-articles-list')
art_tags = vse_stat.find_all('article')
for art_tag in art_tags:
    h2_tag = art_tag.find('h2',class_='tm-title')
    a_tag = h2_tag.find('a')
    link = a_tag['href']
    full_link = f'{site1}{link}'
    time_tag = art_tag.find('time')
    time_pub = time_tag['datetime']
    title = h2_tag.text

    go_to_link = requests.get(full_link,headers=get_headers())
    go_to_link_data = go_to_link.text
    go_to_link_soup = bs4.BeautifulSoup(go_to_link_data,features='lxml')
    full_hodim = go_to_link_soup.find('div', id= 'post-content-body')
    text = full_hodim.text
    for keyword in KEYWORDS:
        if keyword in text:


            pars_data.append({
                'title': title,
                'time_pub': time_pub,
                'link': full_link,


    })


for pars in pars_data:
    print(f'Дата статьи {pars['time_pub']}, Заголовок : {pars['title']}, Ссылка на статью {pars['link']}')


