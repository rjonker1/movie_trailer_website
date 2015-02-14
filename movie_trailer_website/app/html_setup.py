from utils import html_for_movie_trailer_builder
import db.movie_database

#get the top rated movies
movie_database = db.movie_database.MovieDatabase()
top_six_rated_movies_to_display = movie_database.get_top_six_rated_movies()

movie_trailer_html = html_for_movie_trailer_builder.HtmlForMovieTrailerBuilder(top_six_rated_movies_to_display)
movie_trailer_html.open_movies_page()