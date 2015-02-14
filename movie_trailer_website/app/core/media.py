class Media(object):
    """Base class to hold basic information for media related objects to be displayed on a web page. Properties include: title, storyline, poster image url, release year and a user's rating"""
    def __init__(self, title, storyline, poster_image_url, release_year, rating):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.release_year = release_year
        self.rating = rating