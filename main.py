import sqlalchemy
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:hOLODNo12345!@localhost:5432/DZ_PSQL'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name='Александр Сергеевич Пушкин')
publisher2 = Publisher(name='Харуки Мураками')
publisher3 = Publisher(name='Чак Паланик')

session.add_all([publisher1, publisher2, publisher3])
session.commit()

book1 = Book(name='Метель', publisher=publisher1)
book2 = Book(name='Капитанская дочка', publisher=publisher1)
book3 = Book(name='Сказка о царе Салтане', publisher=publisher1)
book4 = Book(name='Евгений Онегин', publisher=publisher1)
book5 = Book(name='Пиковая Дама', publisher=publisher1)
book6 = Book(name='Дубровский', publisher=publisher1)
book7 = Book(name='Норвежский лес', publisher=publisher2)
book8 = Book(name='1084', publisher=publisher2)
book9 = Book(name='Подземка', publisher=publisher2)
book10 = Book(name='Охота на овец', publisher=publisher2)
book11 = Book(name='Колыбельная', publisher=publisher3)
book12 = Book(name='Удушье', publisher=publisher3)
book13 = Book(name='Бойцовский клуб', publisher=publisher3)
book14 = Book(name='Призраки', publisher=publisher3)
book15 = Book(name='Снафф', publisher=publisher3)

session.add_all([book1, book2, book3, book4, book5, book6, book7, book8, book9, book10, book11, book12, book13, book14, book15])
session.commit()

shop1 = Shop(name='Альпина')
shop2 = Shop(name='Лабиринт')
shop3 = Shop(name='Читай город')

session.add_all([shop1, shop2, shop3])
session.commit()

stock1 = Stock(book=book1, shop=shop1, count=1)
stock2 = Stock(book=book2, shop=shop3, count=34)
stock3 = Stock(book=book3, shop=shop3, count=12)
stock4 = Stock(book=book4, shop=shop2, count=7)
stock5 = Stock(book=book5, shop=shop1, count=9)
stock6 = Stock(book=book6, shop=shop2, count=4)
stock7 = Stock(book=book7, shop=shop1, count=20)
stock8 = Stock(book=book8, shop=shop2, count=3)
stock9 = Stock(book=book9, shop=shop3, count=17)
stock10 = Stock(book=book10, shop=shop2, count=2)
stock11 = Stock(book=book11, shop=shop3, count=14)
stock12 = Stock(book=book12, shop=shop2, count=45)
stock13 = Stock(book=book13, shop=shop1, count=10)
stock14 = Stock(book=book14, shop=shop1, count=4)
stock15 = Stock(book=book15, shop=shop1, count=19)

session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9, stock10, stock11, stock12, stock13, stock14, stock15])
session.commit()

sale1 = Sale(price=600, data_sale='07-12-2022', stock=stock1)
sale2 = Sale(price=1100, data_sale='22-12-2022', stock=stock2)
sale3 = Sale(price=500, data_sale='12-11-2019', stock=stock3)
sale4 = Sale(price=700, data_sale='03-03-2021', stock=stock4)
sale5 = Sale(price=900, data_sale='06-02-2023', stock=stock5)
sale6 = Sale(price=400, data_sale='17-01-2023', stock=stock6)
sale7 = Sale(price=800, data_sale='22-11-2020', stock=stock7)
sale8 = Sale(price=1200, data_sale='13-01-2023', stock=stock8)
sale9 = Sale(price=300, data_sale='10-07-2017', stock=stock9)
sale10 = Sale(price=690, data_sale='24-11-2021', stock=stock10)
sale11 = Sale(price=560, data_sale='03-06-2014', stock=stock11)
sale12 = Sale(price=750, data_sale='22-10-2018', stock=stock12)
sale13 = Sale(price=1300, data_sale='04-01-2023', stock=stock13)
sale14 = Sale(price=150, data_sale='27-12-2022', stock=stock14)
sale15 = Sale(price=1000, data_sale='01-01-2023', stock=stock15)

session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, sale9, sale10, sale11, sale12, sale13, sale14, sale15])
session.commit()

# for c in session.query(Publisher).filter(Publisher.name.like('%Пушкин%')).all():
#     print(c)

# c_r = input('Введите имя автора:')

# c_r = input('Введите имя автора:')
# for c in session.query(Publisher).join(Book.publisher).all():
#     print(c)

# session.query(Publisher).join(Book.publisher).all()
# session.query(Publisher).join(Stock.publisher).all()
# session.query(Publisher).join(Shop.publisher).all()
# session.query(Publisher).join(Sale.publisherч).all()

# session.query(
#     Book.title,
#     Shop.name,
#     Stock.count,
#     Sale.data_sale
# ).join(Stock).join(Shop).join(Sale).filter(...).all()
#
# join(Stock.book).join(Stock.shop).join(Sale.stock).filter(Publisher.name == c_r)

def custom():
    c_r = str(input('Введите имя автора: '))
    for r in session.query(
        Book.name,
        Shop.name,
        Sale.price,
        Sale.data_sale
    ).join(Book).join(Shop).join(Sale).filter(Publisher.name == c_r).all():
        print(r)

print(custom())

session.close()
