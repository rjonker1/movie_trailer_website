from utils import html_for_movie_trailer_builder
import db.movie_database

#get the top rated movies
movies = db.movie_database.get_top_five_rated_movies()

movie_trailer_html = html_for_movie_trailer_builder.HtmlForMovieTrailerBuilder(movies)
movie_trailer_html.open_movies_page()