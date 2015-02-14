from core import movie
from core import media

class MovieDatabase():
    """Movie database holding a list of all the movies. Includes functions to return movies by rating or the top six rated movies"""
    def __init__(self):
        self.movie_list = []
        self.movie_list.append(movie.Movie("A Clockwork Orange", "In future Britain, charismatic delinquent Alex DeLarge is jailed and volunteers for an experimental aversion therapy developed by the government in an effort to solve society's crime problem - but not all goes according to plan.", "http://mtv.mtvnimages.com/shared/media/images/acovers/standard/dra100/a175/a17588n7cit.jpg", "https://www.youtube.com/watch?v=G7fO3bzPeBQ", 1971, 5,"Stanley Kubrick"))
        self.movie_list.append(movie.Movie("Full Metal Jacket", "A pragmatic U.S. Marine observes the dehumanizing effects the U.S.-Vietnam War has on his fellow recruits from their brutal boot camp training to the bloody street fighting in Hue.", "http://www.impawards.com/1987/posters/full_metal_jacket.jpg", "https://www.youtube.com/watch?v=x9f6JaaX7Wg", 1987, 4,"Francesca Cima, Stanley Kubrick"))
        self.movie_list.append(movie.Movie("Taxi Driver", "A mentally unstable Vietnam war veteran works as a night-time taxi driver in New York City where the perceived decadence and sleaze feeds his urge for violent action, attempting to save a preadolescent prostitute in the process.", "http://www.newslinemagazine.com/wp-content/uploads/2014/10/taxidriver-1976-film-poster.jpg", "https://www.youtube.com/watch?v=sLpMx8_TYOo", 1976, 5,"Martin Scorsese"))
        self.movie_list.append(movie.Movie("Straw Dogs", "David Sumner (Dustin Hoffman), a mild-mannered academic from the United States, marries Amy (Susan George), an Englishwoman. In order to escape a hectic stateside lifestyle, David and his wife relocate to the small town in rural Cornwall where Amy was raised. There, David is ostracized by the brutish men of the village, including Amy's old flame, Charlie (Del Henney). Eventually the taunts escalate, and two of the locals rape Amy. This sexual assault awakes a shockingly violent side of David.", "http://ia.media-imdb.com/images/M/MV5BMTI4NDY3MTYwMV5BMl5BanBnXkFtZTYwNDkyNDg5._V1_SY317_CR5,0,214,317_AL_.jpg", "https://www.youtube.com/watch?v=yXkqGVfm1mo", 1971, 4, "Sam Peckinpah"))
        self.movie_list.append(movie.Movie("Trainspotting", "Heroin addict Mark Renton (Ewan McGregor) stumbles through bad ideas and sobriety attempts with his unreliable friends -- Sick Boy (Jonny Lee Miller), Begbie (Robert Carlyle), Spud (Ewen Bremner) and Tommy (Kevin McKidd). He also has an underage girlfriend, Diane (Kelly Macdonald), along for the ride. After cleaning up and moving from Edinburgh to London, Mark finds he can't escape the life he left behind when Begbie shows up at his front door on the lam, and a scheming Sick Boy follows.","https://folhasdepapel.files.wordpress.com/2009/06/trainspotting.jpg","https://www.youtube.com/watch?v=R2GKVtWsXKY", 1996, 5, "Danny Boyle"))
        self.movie_list.append(movie.Movie("Fight Club", "A depressed man (Edward Norton) suffering from insomnia meets a strange soap salesman named Tyler Durden (Brad Pitt) and soon finds himself living in his squalid house after his perfect apartment is destroyed. The two bored men form an underground club with strict rules and fight other men who are fed up with their mundane lives. Their perfect partnership frays when Marla (Helena Bonham Carter), a fellow support group crasher, attracts Tyler's attention.","http://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg","https://www.youtube.com/watch?v=SUXWAEX2jlg", 1999, 4, "David Fincher"))
        self.movie_list.append(movie.Movie("Snatch", "Illegal boxing promoter Turkish (Jason Statham) convinces gangster Brick Top (Alan Ford) to offer bets on bare-knuckle boxer Mickey (Brad Pitt) at his bookie business. When Mickey does not throw his first fight as agreed, an infuriated Brick Top demands another match. Meanwhile, gangster Frankie Four Fingers (Benicio Del Toro) comes to place a bet for a friend with Brick Top's bookies, as multiple criminals converge on a stolen diamond that Frankie has come to London to sell","http://static.tvtropes.org/pmwiki/pub/images/Snatch.jpg","https://www.youtube.com/watch?v=lUloT3Dh3-E", 1999, 5, "Guy Ritchie"))
     
    def get_top_six_rated_movies(self):
        top_rated_movies = sorted(self.movie_list, reverse=True) #get the top rated movies based on rating
        return top_rated_movies[:6]

    def get_movies_with_rating_by_rating(self,rating):
        top_movies_with_five_rating = [x for x in self.movie_list if x.rating >= rating] #get all the movies with a rating of 5
        return top_movies_with_five_rating