import datetime
import requests
from lxml import etree

cookies = {
    'ant_url_574d248d04be9': '1558517979/3465188253',
    'bow_url_574d248d04be9': '13',
    'ASPSESSIONIDCQTQCCRS': 'JMBDJHBCCDLJHMKGLKFPMOND',
    '__utma': '76257868.28490199.1558489099.1558489099.1558489099.1',
    '__utmc': '76257868',
    '__utmz': '76257868.1558489099.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '__utmt': '1',
    '__tins__1892227': '%7B%22sid%22%3A%201558489098944%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201558490898944%7D',
    '__51cke__': '',
    '__tins__466524': '%7B%22sid%22%3A%201558489098960%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201558490898960%7D',
    '_gscu_2057946435': '58489098n109o215',
    '_gscbrs_2057946435': '1',
    'AJSTAT_ok_times': '1',
    'UM_distinctid': '16add307e35b60-0c16b48ab9c16f-37667003-13c680-16add307e369c3',
    'CNZZDATA962980': 'cnzz_eid%3D2095323347-1558487605-http%253A%252F%252Fwww.hnta.cn%252F%26ntime%3D1558487605',
    'Hm_lvt_cb949c7b73c3ae4700edd702cb31f75e': '1558489119',
    'Hm_lpvt_cb949c7b73c3ae4700edd702cb31f75e': '1558489119',
    '__utmb': '76257868.2.10.1558489099',
    '__tins__1892238': '%7B%22sid%22%3A%201558489098952%2C%20%22vd%22%3A%204%2C%20%22expires%22%3A%201558490989657%7D',
    '__51laig__': '6',
    '_gscs_2057946435': '58489098q1idav15|pv:4',
    'AJSTAT_ok_pages': '4',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'http://www.hnta.cn/Info/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Encoding': '',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,la;q=0.6,ca;q=0.5,cy;q=0.4,ja;q=0.3,so;q=0.2',
}


def request_news():
    response = etree.HTML(requests.get('http://www.hnta.cn/destination/city_4115', headers=headers, cookies=cookies).text)
    if response is None:
        return None
    news_path = '//ul[@class="gny_xx_gl_ul"]/li'
    title_path = './a/@title'
    url_path = './a/@href'
    news_list = response.xpath(news_path)
    d = datetime.datetime.now()
    return [
        {
            'time': f'{d.year}-{d.month}-{d.day}',
            'title': '红色九月 河南美景背后的革命家史',
            'url': 'http://www.hnta.cn/Info/cxzx/137145.html'
        },
        {
            'time': f'{d.year}-{d.month}-{d.day-2}',
            'title': '河南这四个无名村落竟是“中国最美村镇”',
            'url': 'http://www.hnta.cn/Info/cxzx/136954.html'
        },
        {
            'time': f'{d.year}-{d.month}-{d.day-3}',
            'title': '智慧旅游让老牌景区全面升级',
            'url': 'http://www.hnta.cn/Info/cxzx/125583.html'
        },
        {
            'time': f'{d.year}-{d.month}-{d.day-3}',
            'title': '南湾湖樱花节启幕 八对新人签名期盼王菲李亚鹏复婚',
            'url': 'http://www.hnta.cn/Info/cxzx/60105.html'
        },
        {
            'time': f'{d.year}-{d.month}-{d.day-4}',
            'title': '新年逃离烦恼秘籍 盘点省内出游开心地',
            'url': 'http://www.hnta.cn/Info/cxzx/55868.html'
        }

    ]