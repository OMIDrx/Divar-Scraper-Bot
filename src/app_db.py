from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///Divar.db', echo=False)


Base = declarative_base()


class Ad(Base):

    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    price = Column(String)
    link = Column(String)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sessionlocal = Session()

def insert_ad(title, price, link):
    
    ad = Ad(
        title=title,
        price=price,
        link=link
    )

    sessionlocal.add(ad)
    sessionlocal.commit()
    
    
def get_all_ads():
    
    ads = sessionlocal.query(Ad).all()

    result = []

    for ad in ads:

        result.append({
            'id': ad.id,
            'title': ad.title,
            'price': ad.price,
            'link': ad.link
        })

    return result

def delete_all_ads():
    
    sessionlocal.query(Ad).delete()

    sessionlocal.commit()
    
    
def search_ads(keyword):
    
    ads = sessionlocal.query(Ad).filter(
        Ad.title.like(f'%{keyword}%')
    ).all()

    result = []

    for ad in ads:

        result.append({
            'title': ad.title,
            'price': ad.price,
            'link': ad.link
        })

    return result

def delete_all_ads():
    
    sessionlocal.query(Ad).delete()

    sessionlocal.commit()