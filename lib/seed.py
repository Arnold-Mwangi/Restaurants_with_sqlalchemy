from faker import Faker
import random
from models import engine, session, Restaurants, Customers

if __name__ == '__main__':
    session.query(Restaurants).delete()
    session.query(Customers).delete()

    fake = Faker()

    restaurants = []
    for j in range(50):
        restaurant = Restaurants(
            name=fake.unique.company(),
            price=random.randint(1000, 50000)
        )

        session.add(restaurant)
        restaurants.append(restaurant)
        session.commit()

    customers = []
    for i in range(50):
        customer = Customers(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )

        session.add(customer)
        customers.append(customer)

        session.commit()
