import imdb
film = imdb.IMDb()
search = film.get_top250_movies()
for i in range(25):
    print(search[i])
