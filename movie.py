class Movie():

    def __init__(self, title, year, rank, imageUrl):
        self.title = title
        self.year = year
        self.rank = rank
        self.imageUrl = imageUrl

    def movieJSON(self):
        return {
            "title": self.title,
            "year": self.year,
            "rank": self.rank,
            "imageUrl": self.imageUrl
        }

        