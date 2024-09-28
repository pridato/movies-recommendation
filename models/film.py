class Movie:
    def __init__(
        self, id: str, title: str, genre: str, duration: int, director: str, actor: str
    ) -> None:
        self.id = id
        self.title = title
        self.genre = genre
        self.duration = duration  # in minutes
        self.director = director
        self.actor = actor

    def __repr__(self) -> str:
        return f"Movie(id='{self.id}', title='{self.title}', genre='{self.genre}', duration={self.duration}, director='{self.director}'), actor='{self.actor}'"
