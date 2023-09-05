# Restaurant Review Domain

This project is a Python application that simulates a restaurant review domain using SQLAlchemy, a popular Object-Relational Mapping (ORM) library for Python. The application consists of three main models: `Restaurant`, `Review`, and `Customer`, each representing a key entity in the restaurant review system. These models are interconnected through various relationships to capture the complex interactions between customers, restaurants, and reviews.

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Features](#features)
- [Usage](#usage)
- [Example Queries](#example-queries)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with this project, you should have the following prerequisites installed on your system:

- Python 3.x
- SQLAlchemy
- SQLite (for database storage)

Clone the project repository to your local machine:

git clone https://github.com/Arnold-Mwangi/Restaurants_with_sqlalchemy
cd Restaurants_with_sqlalchemy

`~Run pipenv install`





## Project Structure

The project structure is organized as follows:

- `models.py`: Contains the SQLAlchemy models for `Restaurant`, `Review`, and `Customer`.
- `seeds.py`: Provides seed data to populate the database for testing.
- `README.md`: The project's README file.
- `app.py`: A sample application demonstrating the use of the models and relationships.

## Database Schema

The database schema consists of three tables:

- `restaurants`: Stores information about restaurants, including their name and price.
- `customers`: Contains details about customers, such as their first name and last name.
- `reviews`: Represents reviews submitted by customers for specific restaurants. This table includes a `star_rating` column to store review ratings.

The relationships between these tables are defined as follows:

- `Restaurant` has a one-to-many relationship with `Review` (one restaurant can have many reviews).
- `Customer` also has a one-to-many relationship with `Review` (one customer can have many reviews).
- `Review` belongs to both `Restaurant` and `Customer`.

## Features

This project demonstrates several features related to restaurant reviews:

- Creating and querying restaurant, customer, and review objects using SQLAlchemy.
- Establishing relationships between `Restaurant`, `Customer`, and `Review`.
- Retrieving restaurant reviews and customers who reviewed a restaurant.
- Getting reviews left by a customer and restaurants reviewed by a customer.
- Implementing aggregate and relationship methods, such as calculating a customer's favorite restaurant and adding/deleting reviews.

## Usage

To use the project, you can create instances of `Restaurant`, `Customer`, and `Review` classes and manipulate the data as needed. You can also implement custom methods for your specific use cases, such as calculating statistics or generating reports.

The provided `seeds.py` file allows you to create sample data to test your models and relationships. You can customize the seed data to match your requirements.

## Example Queries

Here are some example queries and methods that you can use with this project:

- `session.query(Customer).first().restaurants`: Retrieves a list of restaurants for the first customer in the database based on seed data.
- `session.query(Review).first().customer`: Returns the customer for the first review in the database.
- `session.query(Restaurant).first().reviews()`: Gets all reviews for a specific restaurant.
- `session.query(Restaurant).first().customers()`: Retrieves all customers who reviewed a specific restaurant.
- `session.query(Customer).first().reviews()`: Gets all reviews left by a specific customer.
- `session.query(Customer).first().restaurants()`: Retrieves all restaurants reviewed by a specific customer.
- `session.query(Customer).first().full_name()`: Returns the full name of the first customer in Western style.
- `session.query(Customer).first().favorite_restaurant()`: Retrieves the restaurant instance with the highest star rating from the first customer.
- `session.query(Customer).first().add_review(restaurant_instance, rating)`: Adds a new review for a restaurant by the first customer.
- `session.query(Customer).first().delete_reviews(restaurant_instance)`: Removes all reviews by the first customer for a specific restaurant.
- `session.query(Review).first().full_review()`: Generates a formatted review string for the first review in the database.
- `Restaurant.fanciest()`: Returns a restaurant instance for the restaurant with the highest price.
- `session.query(Restaurant).first().all_reviews()`: Retrieves a list of formatted review strings for the first restaurant's reviews.

## Contributing

Contributions to this project are welcome! If you have suggestions, bug reports, or would like to add new features, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
