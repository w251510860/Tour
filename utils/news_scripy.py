import requests
from lxml import etree


def request_news():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'http://www.xyta.net/'
    response = etree.HTML(requests.get(url, headers=headers).text)
    if response is None:
        return None
    news_path = '//*[@id="tbc_01"]/ul/li'
    time_path = './i/text()'
    title_path = './a/@title'
    url_path = './a/@href'
    news_list = response.xpath(news_path)
    return [
        {
            'time': item.xpath(time_path)[0],
            'title': item.xpath(title_path)[0],
            'url': item.xpath(url_path)[0]
        } for item in news_list
    ]
