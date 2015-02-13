import os
import webbrowser

def get_movie_trailer_web_page():
    dir = os.path.abspath(os.curdir)
    view = os.path.join(dir,r"app\views\movie_trailers.html")
    return view

def open_html_page_web_browser(file):
    url = os.path.abspath(file.name)
    webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
