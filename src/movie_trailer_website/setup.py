from distutils.core import setup

setup(
    # Application name:
    name="app",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Rudi Jonker",
    author_email="rdjnkr@gmailcom",

    # Packages
    packages=["app"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/rjonker1/movie_trailer_website",

    #
    # license="LICENSE.txt",
    description="Serve html page with a list of movies to a web browser allowing users to view information about the movie and watch it's trailer",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    
    )