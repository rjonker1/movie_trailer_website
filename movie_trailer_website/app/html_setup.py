from utils import html_for_movie_trailer_builder
import db.movie_database


movie_database = db.movie_database.MovieDatabase()

#get the top six rated movies from the movie database
top_six_rated_movies_to_display = movie_database.get_top_six_rated_movies()

#build the html using the movie information. Once the html is built. show in the web browser
movie_trailer_html = html_for_movie_trailer_builder.HtmlForMovieTrailerBuilder(top_six_rated_movies_to_display)
movie_trailer_html.open_movies_page()