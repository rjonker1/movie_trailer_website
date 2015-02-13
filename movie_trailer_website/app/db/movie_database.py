from core import movie

movie_list = []
movie_list.append(movie.Movie("A Clockwork Orange", "In future Britain, charismatic delinquent Alex DeLarge is jailed and volunteers for an experimental aversion therapy developed by the government in an effort to solve society's crime problem - but not all goes according to plan.", "http://ia.media-imdb.com/images/M/MV5BMTY3MjM1Mzc4N15BMl5BanBnXkFtZTgwODM0NzAxMDE@._V1_SX640_SY720_.jpg", "https://www.youtube.com/watch?v=G7fO3bzPeBQ", "1999/01/01", "5"))
movie_list.append(movie.Movie("Full Metal Jacket", "A pragmatic U.S. Marine observes the dehumanizing effects the U.S.-Vietnam War has on his fellow recruits from their brutal boot camp training to the bloody street fighting in Hue.", "http://www.impawards.com/1987/posters/full_metal_jacket.jpg", "https://www.youtube.com/watch?v=x9f6JaaX7Wg", "1999/01/01", "5"))
movie_list.append(movie.Movie("Taxi Driver", "A mentally unstable Vietnam war veteran works as a night-time taxi driver in New York City where the perceived decadence and sleaze feeds his urge for violent action, attempting to save a preadolescent prostitute in the process.", "http://www.newslinemagazine.com/wp-content/uploads/2014/10/taxidriver-1976-film-poster.jpg", "https://www.youtube.com/watch?v=sLpMx8_TYOo", "1999/01/01", "5"))


def get_top_five_rated_movies():
    top_rated_movies = [x for x in movie_list if x.rating == "5"] #get all the movies with a rating of 5
    return top_rated_movies[:5]