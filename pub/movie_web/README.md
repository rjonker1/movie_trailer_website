# Movie Trailer Website - Code #

### SUMMARY ###
This is the source code used to display movie and their trailers on a movie trailer html page in the web browser

### PROJECT OVERVIEW ###

	1. The applicaiton is initialized through the bootstrapper.py file, located in \movie_web\app\boostrapper.py
		*. The bootstrapper.py file will get the top rated movies from a movie database, insert each movie's details into an html page and then serve the html into a webbrowser.
	2 The Project consists of the following folders:

		*	content
			*	Holds CSS and Javascript files used in the html pages

		*	core
			*	Contains the core classes used throughout the project. Currently Movie and Media objects are living in there

		*	db
			*	Contains a "movie database" (currently just a list) of movies. The information from this database is what will be used to display on the web page

		*	functions
			*	Not used

		*	utils
			*	Contains helper type functions and classes. Currently has the html content and a builder class which will insert each movie's information into a newly created html page and then, serve this html page to a webbrowser

		*	views
			*	Contains html pages as well as dynamically built html pages. Contains a view_manager.py file which holds the html file's name (e.g. movie_trailers.html) as well as the path to create this html page to and access the html page from

### EXECUITON / RUN ###

	* To execute the source code, build the movie trailer html page and serve it to the web browser, you need to run the bootstrapper.py file from the python shell