import media
class Movie(media.Media):
    """description of class"""
    def __init__(self, title, storyline, poster_image_url, trailer_url, release_date, rating): 
        media.Media.__init__(self, title, storyline, poster_image_url, release_date, rating)
        self.trailer_url = trailer_url