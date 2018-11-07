from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mysql://root:puhao@localhost:3306/qiushi?charset=utf8')


class QushiBean(Base):
    __tablename__ = 'qiushi'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), index=True)
    content = Column(Text)
    image_url = Column(Text)

    def __repr__(self):
        return "name is %s" % self.name


if __name__ == '__main__':
    Base.metadata.create_all(engine)
