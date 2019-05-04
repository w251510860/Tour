from faker import Faker

from Introduce.introduce import mock_introduce_data
from project import db
from project.modules.models import Knowledge, Introduce


def mock_article():
    f = Faker(locale='zh_CN')
    for i in range(1, 100):
        s = Knowledge()
        s.user_id = 1
        s.title = f.word()
        s.content = f.text()
        s.tour_route = f.address()
        s.advice_time = f.date_time()
        db.session.add(s)
        db.session.commit()


def mock_introduce():
    for data in mock_introduce_data:
        s = Introduce()
        s.name = data['name']
        s.title = data['title']
        s.content = data['content']
        db.session.add(s)
        db.session.commit()


