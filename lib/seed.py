from faker import Faker
import random
from models import engine, session, Restaurants, Customers, Reviews

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


reviews = []
star_ratings = [0, 1, 2, 3, 4, 5]

for restaurant in restaurants:
    for i in range(random.randint(1,5)):

        customer = random.choice(customers)
        if restaurant not in customer.restaurants:
            customer.restaurants.append(restaurant)
            session.add(customer)
            session.commit()

        star_rating = random.choice(star_ratings)
        print(f"Star Rating: {star_rating}")

        review = Reviews(
            star_rating=star_rating,
            restaurant_id=restaurant.id,
            customer_id=customer.id
        )
        reviews.append(review)

# for review in reviews:
session.add(review)


session.commit()
session.close()
