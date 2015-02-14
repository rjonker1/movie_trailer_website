import media
import random
class Movie(media.Media):
    """Inherits from the media class and has additional trailer url and directed by properties. 
    Functions include: 
     overloaded comparison operators [__cmp__] used for comparing the rating of a Movie 
     overloaded representation operator [__repr__] function used to represent the Movie properties in the desired format. This has been implemented for sorting purposes """
    def __init__(self, title, storyline, poster_image_url, trailer_url, release_year, rating, directed_by): 
        media.Media.__init__(self, title, storyline, poster_image_url, release_year, rating)
        self.trailer_url = trailer_url
        self.directed_by = directed_by
    def __repr__(self):
        return "{}: {} {} {} {} {} {} {}".format(self.__class__.__name__, self.title, self.storyline, self.poster_image_url, self.release_year, self.rating, self.directed_by)
    def __cmp__(self, other):
        if hasattr(other, "rating"):
            return self.rating.__cmp__(other.rating)