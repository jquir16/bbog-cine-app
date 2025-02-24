class Movie:
    def __init__(self, id, title, overview, director, casting, release_date, start_date, end_date, runtime, mpaa):
        self.id = id
        self.title = title
        self.overview = overview
        self.director = director
        self.casting = casting
        self.release_date = release_date
        self.start_date = start_date
        self.end_date = end_date
        self.runtime = runtime
        self.mpaa = mpaa
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "overview": self.overview,
            "director": self.director,
            "casting": self.casting,
            "release_date": self.release_date,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "runtime": self.runtime,
            "mpaa": self.mpaa,
        }