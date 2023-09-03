from sqlalchemy import create_engine, Integer, Column, Index, Table, String, Foreignkey, DateTime, MetaData, func
from sqlalchemy.orm import sessionmaker, declarative_base


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}    

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)


engine = create_engine('sqlite:///restaurants.db')

Session = sessionmaker(bind = engine)
session = Session()

class Restaurants(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price=Column(Integer)

    def __repr__(self):
        return f"name:: {self.name}: price::{self.price}"



class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)