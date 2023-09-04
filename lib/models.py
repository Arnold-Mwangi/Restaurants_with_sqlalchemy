from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}    

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)


engine = create_engine('sqlite:///restaurants.db')

Session = sessionmaker(bind = engine)
session = Session()



class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price=Column(Integer)

    # def __repr__(self):
    #     return f"name:: {self.name}: price::{self.price}"

    reviews = relationship('Review', back_populates='restaurant')
    customers = association_proxy('reviews', 'customer', 
        creator = lambda cu: Reviews(customer = cu))

    def reviews(self):
        # query = session.query(Reviews)
        # print((query))
        return self.reviews

    def customers(self):
        return self.customers



class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', back_populates='customer')
    restaurants = association_proxy('reviews', 'restaurant',
        creator=lambda re: Reviews(restaurant = re))

    def reviews(self):
        return self.reviews

    def restaurants(self):
        return [review.restaurant for review in self.reviews]


class Review(Base):
    __tablename__ = 'reviews'

    id=Column(Integer(), primary_key=True)
    star_rating=Column(Integer())
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')


    def __repr__(self):
        return f"id={self.id}, rating = {self.star_rating} customer={self.customer_id} for restaurant::{self.restaurant_id}"

    def customer(self):
        query = session.query(Customer).filter_by(id = self.customer_id).first()
        return query

    def restaurant(self):
        return self.restaurant


review1 = Review()