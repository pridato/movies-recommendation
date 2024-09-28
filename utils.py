from typing import List
from consts import (
    films,
    max_users,
    directors,
    genres,
    actors,
    min_duration,
    max_duration,
    min_rating,
    max_rating,
)
from models.user import User
from models.film import Movie
import random


def avarage_rating(users: List[User], film: str) -> float:
    """
    Function that returns the average rating for a given film
    @param users: List[User] - list of users
    @param film: str - film name
    @return: float - average rating
    """
    # each user has a fealm, we iterate over all and append the rating
    ratings = [user.rating for user in users if user.film.title == film]
    return round(sum(ratings) / len(ratings), 2)


def create_data() -> List[User]:
    """
    Function to create data from consts
    @return
    """
    users = []
    for id, name_movie in enumerate(films):
        movie = Movie(
            str(id),
            name_movie,
            random.choice(genres),
            random.randint(min_duration, max_duration),
            random.choice(directors),
            random.choice(actors),
        )
        for user in range(max_users):
            if random.randint(0, 1) == 1:
                rating = random.randint(min_rating, max_rating)
                users.append(User(user, movie, rating))

    return users
