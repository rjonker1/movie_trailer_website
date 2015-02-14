class HtmlForMovieTrailer(object):
    """Holds static html to display Movie information. The CSS and Javascript files can be found in the content directory of this project.
    There are three properties:
    movie_page_head: html to display the head elements and includes links to style sheets and java script files
    movie_page_content: html to display the main page body content within the body elements
    movie_tile_content: html to hold information for each movie trailer's information """
    def __init__(self):
        self.movie_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Soooper Movies</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" type="text/css" href="../content/css/default.css" />
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>    
    <script type="text/javascript" src="../content/js/common.js"></script>
</head>
'''
        self.movie_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Soooper Movies</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''
        self.movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title} <span class="release-year">({release_year})</span></h2>    
    <h5>Average Rating: <span class="ratings">{rating}</span>/5</h4>    
    <p class="movie-storyline">{storyline}</p>
    <h3>Directed By: <span class="directed-by">{directed_by}</span></h2>
</div>
'''