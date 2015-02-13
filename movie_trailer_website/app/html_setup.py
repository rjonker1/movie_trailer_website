import sys
from core import movie
from utils import html_for_movie_trailer_builder
print(sys.path)


a_clock_work_orange = movie.Movie("A Clockwork Orange", "In future Britain, charismatic delinquent Alex DeLarge is jailed and volunteers for an experimental aversion therapy developed by the government in an effort to solve society's crime problem - but not all goes according to plan.", "http://ia.media-imdb.com/images/M/MV5BMTY3MjM1Mzc4N15BMl5BanBnXkFtZTgwODM0NzAxMDE@._V1_SX640_SY720_.jpg", "https://www.youtube.com/watch?v=G7fO3bzPeBQ", "1999/01/01", "5")

full_metal_jacket = movie.Movie("Full Metal Jacket", "A pragmatic U.S. Marine observes the dehumanizing effects the U.S.-Vietnam War has on his fellow recruits from their brutal boot camp training to the bloody street fighting in Hue.", "http://www.impawards.com/1987/posters/full_metal_jacket.jpg", "https://www.youtube.com/watch?v=x9f6JaaX7Wg", "1999/01/01", "5")

taxi_driver = movie.Movie("Taxi Driver", "A mentally unstable Vietnam war veteran works as a night-time taxi driver in New York City where the perceived decadence and sleaze feeds his urge for violent action, attempting to save a preadolescent prostitute in the process.", "http://www.newslinemagazine.com/wp-content/uploads/2014/10/taxidriver-1976-film-poster.jpg", "https://www.youtube.com/watch?v=sLpMx8_TYOo", "1999/01/01", "5")

movies = [a_clock_work_orange, full_metal_jacket, taxi_driver]

movie_trailer_html = html_for_movie_trailer_builder.HtmlForMovieTrailerBuilder(movies)
movie_trailer_html.open_movies_page()