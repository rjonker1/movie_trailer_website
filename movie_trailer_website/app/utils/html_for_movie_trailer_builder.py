import urlparse, urllib, re
import html_for_movie_trailer
import views.view_manager

class HtmlForMovieTrailerBuilder(html_for_movie_trailer.HtmlForMovieTrailer):
    """description of class"""
    def __init__(self, movies):
        html_for_movie_trailer.HtmlForMovieTrailer.__init__(self)
        self.movies = movies

    def create_movie_content(self):
        content = ''
        for movie in self.movies: 
            # Extract the youtube ID from the url
            id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_url)
            id_match = id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_url)
            trailer_id = id_match.group(0) if id_match else None

            # Append the tile for the movie with its content filled in
            content += self.movie_tile_content.format(
                movie_title=movie.title,
                poster_image_url=movie.poster_image_url,
                trailer_id=trailer_id,
                release_year=movie.release_year,
                rating=movie.rating,
                storyline=movie.storyline,
                directed_by=movie.directed_by)
           
        return content

    def open_movies_page(self):
        # Create or overwrite the output file
        movie_trailer_view = views.view_manager.get_movie_trailer_web_page()
        output_file = open(movie_trailer_view,'w')
        
        # Replace the placeholder for the movie tiles with the actual dynamically generated content
        rendered_content = self.movie_page_content.format(movie_tiles=self.create_movie_content())

        # Output the file
        output_file.write(self.movie_page_head + rendered_content)
        output_file.close()

        # open the out file in the browser
        views.view_manager.open_html_page_web_browser(output_file)