1. SUMMARY
This is the source code used to display movie and their trailers on a movie trailer html page in the web browser

2. PROJECT OVERVIEW

	2.1 The applicaiton is initialized through the bootstrapper.py file, located in \movie_web\app\boostrapper.py
		2.1. The bootstrapper.py file will get the top rated movies from a movie database, insert each movie's details into an html page and then serve the html into a webbrowser.
	2.2 The Project consists of the following folders:

		2.2.1 content
			  Holds CSS and Javascript files used in the html pages

		2.2.2 core
			  Contains the core classes used throughout the project. Currently Movie and Media objects are living in there

		2.2.3 db
			  Contains a "movie database" (currently just a list) of movies. The information from this database is what will be used to display on the web page

		2.2.4 functions
			  Not used

		2.3.5 utils
			  Contains helper type functions and classes. Currently has the html content and a builder class which will insert each movie's information into a newly created html page 
			  and then, serve this html page to a webbrowser

		2.3.6 views
			  Contains html pages as well as dynamically built html pages. Contains a view_manager.py file which holds the html file's name (e.g. movie_trailers.html) as well as the path to 
			  create this html page to and access the html page from

3. EXECUITON / RUN
	3.1 To execute the source code, build the movie trailer html page and serve it to the web browser, you need to run the bootstrapper.py file from the python shell