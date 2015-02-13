import os
import webbrowser

class ViewManager(object):
    """description of class"""
    def __init__(self):
        self.web_trailer_html = "movie_trailers.html"

    def open_movie_trailer_page_in_webbrowser(self):
        print("Opening page...")
        print(os.path)
        movie_trailer_html = open(self.web_trailer_html,"r")
        url = os.path.abspath(self.movie_trailer_html.name)
        webbrowser.open('file://' + url, new=2) # open in a new tab, if possible

