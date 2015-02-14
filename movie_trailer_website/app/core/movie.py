import media
import random
class Movie(media.Media):
    """description of class"""
    def __init__(self, title, storyline, poster_image_url, trailer_url, release_year, rating, directed_by): 
        media.Media.__init__(self, title, storyline, poster_image_url, release_year, rating)
        self.trailer_url = trailer_url
        self.directed_by = directed_by
    def __repr__(self):
        return "{}: {} {} {} {} {} {}".format(self.__class__.__name__,self.title,self.storyline,self.poster_image_url,self.release_year,self.rating)
    def __cmp__(self,other):
        if hasattr(other,"rating"):
            return self.rating.__cmp__(other.rating)