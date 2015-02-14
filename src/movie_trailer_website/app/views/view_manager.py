import os
import webbrowser

#function to get the current directory of the view folder which holds the movie trailer html page which will be displayed in a web browser
def get_movie_trailer_web_page():
    dir = os.path.abspath(os.curdir)    
    view = os.path.join(dir + "\\",r"app\views\movie_trailers.html")
    return view

#opens a passed in file in the web browser
def open_html_page_web_browser(file):
    url = os.path.abspath(file.name)
    webbrowser.open('file://' + url, new=2)
