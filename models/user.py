import random


class User:
    def __init__(self, user, film, rating) -> None:
        self.id = str(random.randint(0, 100))
        self.user = user
        self.film = film
        self.rating = rating

    def __repr__(self) -> str:
        return f"User(id='{self.id}',user='{self.user}, film='{self.film}', rating={self.rating})"
