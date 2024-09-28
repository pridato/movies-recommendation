from utils import create_data, avarage_rating
from consts import films
from plotlib import plot_data

if __name__ == "__main__":
    users = create_data()
    ratings = []
    for film in films:
        rating = avarage_rating(users, film)
        ratings.append((film, rating))

    ratings.sort(key=lambda x: x[1], reverse=True)
    plot_data(
        len(users), [film for film, _ in ratings], [rating for _, rating in ratings]
    )
